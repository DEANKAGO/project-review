from django.urls import path
from . import views

urlpatterns = [
  path('', views.homepage, name='home'),
  path('search', views.search_profile, name = 'search_profile'),

]