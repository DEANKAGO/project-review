from django.shortcuts import render, redirect
from .models import *
# from __future__ import unicode_literals
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
# from .forms import profileForm,UserUpdateForm,RegistrationForm,projectForm,UpdateUserProfileForm,RateForm
from django.shortcuts import get_object_or_404
from django.http import HttpResponseRedirect
from django.contrib.auth.models import User
from django.urls import reverse
from rest_framework.response import Response
from rest_framework.views import APIView
# from .serializer import ProfileSerializer,ProjectSerializer

# Create your views here.

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
        return render(request, 'search.html', params)
    else:
        message = "You haven't searched for any profile"
    return render(request, 'search.html', {'message': message})

