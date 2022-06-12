from django.shortcuts import render
from .models import *

# Create your views here.

def homepage(request):
  return render(request, 'main/index.html')


def rating(request, slug):
  profile = Profile.objects.get(slug=slug)
  projects = Project.objects.filter(profile=profile).order_by('-date_created')
  return render(request, 'main/rating.html', locals())


def search_profile(request):
  if 'profile' in request.GET and request.GET['profile']:
    searched_item = request.GET['profile']
    profiles = Profile.searching_profile(searched_item)
    term = f"{searched_item}"
    return render(request, 'main/search.html', locals())
  else:
    term = "kindly input a profile name"
    return render(request, 'main/search.html', locals())