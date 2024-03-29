from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from cloudinary.models import CloudinaryField
from django.contrib.contenttypes.fields import GenericRelation
from star_ratings.models import Rating





# Create your models here.

class Profile(models.Model):
  photo = CloudinaryField('media')
  Bio = models.CharField(max_length=30)
  user = models.OneToOneField(User, on_delete=models.CASCADE)
  date_created = models.DateTimeField(auto_now_add=True)

  def __str__(self):
    return self.user.username

  def save_profile(self):
    self.user

  def delete_profile(self):
    self.delete()

  @classmethod
  def search_profile(cls, name):
    return cls.objects.filter(user__username__icontains=name).all()



class Projects(models.Model):
  title = models.CharField(max_length=30)
  description = models.TextField(max_length=250, null=True, blank=True)
  projects_screenshot = CloudinaryField('media')
  project_url = models.URLField(max_length=250)
  user = models.ForeignKey(Profile, on_delete=models.CASCADE, default='')
  date_created = models.DateTimeField(auto_now_add=True)

  def save_projects(self):
    self.user

  def delete_projects(self):
    self.delete()

  @classmethod
  def search_projects(cls, name):
    return cls.objects.filter(title__icontains=name).all()


RATE_CHOICES = [
(1,'1'),
(2,'2'),
(3,'3'),
(4,'4'),
(5,'5'),
]





class Review(models.Model):
  user = models.ForeignKey(User, on_delete=models.CASCADE)
  projects = models.ForeignKey(Projects, on_delete=models.CASCADE)
  date_created = models.DateTimeField(auto_now_add=True)
  text = models.TextField(max_length=1000, blank = True)
  design = models.PositiveSmallIntegerField(choices = RATE_CHOICES,default= 0)
  usability = models.PositiveSmallIntegerField(choices = RATE_CHOICES,default = 0)
  content = models.PositiveSmallIntegerField(choices = RATE_CHOICES,default = 0)

  class meta:
    unique_together = ('user', 'projects')


  def __str__(self):
    return f"{self.user}'s {self.design} {self.usability} {self.content} for {self.projects}"















