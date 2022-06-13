from django.urls import path, include, re_path
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [
  path('register/',views.register, name='registration'),
  path('', views.index, name='home'),
  path('search/', views.searchprofile, name='search'),
  path('newproject/',views.addProject,name = 'project'),
  path('profile/<id>/',views.profile,name = 'profile'),
  path('editprofile/',views.editprofile,name = 'editprofile'), 
  path('projects/<id>/',views.projects,name = 'projects'),
  path('rate/<id>/',views.rate,name = 'rate')

]