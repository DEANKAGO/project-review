from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import * 



class projectForm(forms.ModelForm):  
  class Meta:
    model = Projects
    fields = ['title','description','projects_screenshot','project_url']


class profileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = [ 'photo', 'Bio']


class UserUpdateForm(forms.ModelForm):
    email = forms.EmailField()
    class Meta:
        model = User
        fields = ['username','email'] 



class UpdateUserProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['Bio', 'photo']