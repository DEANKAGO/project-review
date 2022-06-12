from django.shortcuts import render
from .models import *

# Create your views here.

def homepage(request):
  return render(request, 'main/index.html')


def rating(request):
  return render(request, 'main/rating.html')