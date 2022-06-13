from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import * 



class projectForm(forms.ModelForm):  
  class Meta:
    model = Projects
    fields = ['title','description','projects_screenshot','project_url']