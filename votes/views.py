from __future__ import unicode_literals
from django.shortcuts import render, redirect, get_object_or_404
from .models import *
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from .forms import *
from django.http import HttpResponseRedirect
from django.contrib.auth.models import User
from django.urls import reverse
from rest_framework.response import Response
from rest_framework.views import APIView
from .serializer import ProfileSerializer,ProjectSerializer
from django.http import Http404

# Create your views here.

def register(request):
    if request.method=="POST":
        form=RegistrationForm(request.POST)
        procForm=profileForm(request.POST, request.FILES)
        if form.is_valid() and procForm.is_valid():
            username=form.cleaned_data.get('username')
            user=form.save()
            profile=procForm.save(commit=False)
            profile.user=user
            profile.save()
        return redirect('login')
    else:
        form= RegistrationForm()
        prof=profileForm()
    params={
        'form':form,
        'profForm': prof
    }
    return render(request, 'users/register.html', params)



def index(request):
  projects = Projects.objects.all()
  return render(request, 'main/index.html', {'projects': projects})


def searchprofile(request):
    if 'searchUser' in request.GET and request.GET['searchUser']:
        name = request.GET.get("searchUser")
        searchResults = Projects.search_projects(name)
        message = f'name'
        params = {
            'results': searchResults,
            'message': message
        }
        return render(request, 'main/search.html', params)
    else:
        message = "You haven't searched for any profile"
    return render(request, 'main/search.html', {'message': message})



@login_required(login_url='login') 
def addProject(request):
    current_user = request.user
    user_profile = Profile.objects.get(user = current_user)
    if request.method == 'POST':
        form = projectForm(request.POST,request.FILES)
        if form.is_valid:
            newProj = form.save(commit = False)
            newProj.user = user_profile
            newProj.save()
        return redirect('home')  
    else:
        form = projectForm()
    return render(request,'main/newProject.html',{'form':form})  



@login_required(login_url='login') 
def profile(request,id):
    try:
        prof = Profile.objects.get(user = id)
    except Profile.DoesNotExist:
        raise Http404("No MyModel matches the given query.")
    return render(request,'main/profile.html',{"profile":prof})



def editprofile(request):
    user= request.user
    if request.method == 'POST':
        user_form = UserUpdateForm(request.POST, instance=request.user)
        prof_form = UpdateUserProfileForm(request.POST, request.FILES, instance=request.user.profile)
        if user_form.is_valid() and prof_form.is_valid():
            user_form.save()
            prof_form.save()
            return redirect('profile', user.id)
    else:
        user_form = UserUpdateForm(instance=request.user)
        prof_form = UpdateUserProfileForm(instance=request.user.profile)
    params = {
        'user_form': user_form,
        'prof_form': prof_form
    }
    return render(request, 'main/editprofile.html', params)


def projects(request,id):
    proj = Projects.objects.get(id = id)
    return render(request,'main/readmore.html',{"projects":proj})


@login_required(login_url='login')
def rate(request,id):
    project = Projects.objects.get(id = id)
    user = request.user
    if request.method == 'POST':
        form = RateForm(request.POST)
        if form.is_valid():
            rate = form.save(commit=False)
            rate.user = user
            rate.projects = project
            rate.save()
            return redirect('home')
    else:
        form = RateForm()
    return render(request,"main/rate.html",{"form":form,"project":project}) 



class ProfileList(APIView):
    def get(self,request,format = None):
        all_profile = Profile.objects.all()
        serializerdata = ProfileSerializer(all_profile,many = True)
        return Response(serializerdata.data)



class ProjectList(APIView):
    def get(self,request,format = None):
        all_projects = Projects.objects.all()
        serializerdata = ProjectSerializer(all_projects,many = True)
        return Response(serializerdata.data)

