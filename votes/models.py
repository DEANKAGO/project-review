from django.db import models
from django.utils import timezone
from django.template.defaultfilters import slugify
from django.urls import reverse



# Create your models here.

class Profile(models.Model):
  prof_image = models.ImageField(null=True, blank=True)
  user_bio = models.TextField(blank=True, null=True)
  projects = models.CharField(null=True, blank=True, max_length=180)
  contact = models.CharField(null=True, blank=True, max_length=180)


class Project(models.Model):
  title = models.CharField(null=True, blank=True, max_length=180)
  imagee = models.ImageField(null=True, blank=True)
  description = models.TextField(null=True, blank=True)
  link = models.URLField(null=True, blank=True)
