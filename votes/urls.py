from django.urls import path, include, re_path
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [
  path('register/',views.register, name='registration'),
  path('login/', auth_views.LoginView.as_view(template_name='users/login.html'), name='login'),
  path('logout/', auth_views.LogoutView.as_view(template_name='users/logout.html'), name='logout'),
  path('', views.index, name='home'),
  path('search/', views.searchprofile, name='search'),
  path('newproject/',views.addProject,name = 'project'),
  path('profile/<id>/',views.profile,name = 'profile'),
  path('editprofile/',views.editprofile,name = 'editprofile'), 
  path('projects/<id>/',views.projects,name = 'projects'),
  path('rate/<id>/',views.rate,name = 'rate'),
  path('api/profile',views.ProfileList.as_view()),
  path('api/projects',views.ProjectList.as_view()),
  path('ratings/', include('star_ratings.urls', namespace='ratings')),


]