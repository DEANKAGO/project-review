from django.db import models
from django.utils import timezone
from django.template.defaultfilters import slugify
from django.urls import reverse
from uuid import uuid4
from django.core.validators import MaxLengthValidator, MinLengthValidator



# Create your models here.

class Profile(models.Model):
  title = models.TextField(null=True, blank=True)
  prof_image = models.ImageField(null=True, blank=True, upload_to='media/')
  user_bio = models.TextField(blank=True, null=True)
  projects = models.CharField(null=True, blank=True, max_length=180)
  contact = models.CharField(null=True, blank=True, max_length=180)

  uniqueId = models.CharField(null=True, blank=True, max_length=100)
  slug = models.SlugField(max_length=500, blank=True, null=True, unique=True)
  date_created = models.DateTimeField(blank=True, null=True)
  last_updated = models.DateTimeField(blank=True, null=True)

  def __str__(self):
    return '{} {}'.format(self.title, self.uniqueId)

  def get_absolute_url(self):
    return reverse('profile-detail', kwargs={'slug': self.slug})

  def save(self, *args, **kwargs):
    if self.date_created is None:
      self.date_created = timezone.localtime(timezone.now())
    if self.uniqueId is None:
      self.uniqueId = str(uuid4()).split('-')[4]
      self.slug = slugify('{} {}'.format(self.title, self.uniqueId))

    self.slug = slugify('{} {}'.format(self.title, self.uniqueId))
    self.last_updated = timezone.localtime(timezone.now())
    super(Profile, self).save(*args, **kwargs)


class Project(models.Model):
  title = models.CharField(null=True, blank=True, max_length=180)
  image = models.ImageField(null=True, blank=True, upload_to='media/')
  description = models.TextField(null=True, blank=True)
  link = models.URLField(null=True, blank=True)

  profile = models.ForeignKey(Profile, null=True, blank=True, on_delete=models.CASCADE)

  uniqueId = models.CharField(null=True, blank=True, max_length=100)
  slug = models.SlugField(max_length=500, unique=True, blank=True, null=True)
  date_created = models.DateTimeField(blank=True, null=True)
  last_updated = models.DateTimeField(blank=True, null=True)

  def __str__(self):
    return '{} {}'.format(self.profile.title, self.uniqueId)

  def get_absolute_url(self):
    return reverse('project-detail', kwargs={'slug': self.slug})

  def save(self, *args, **kwargs):
    if self.date_created is None:
      self.date_created = timezone.localtime(timezone.now())
    if self.uniqueId is None:
      self.uniqueId = str(uuid4()).split('-')[4]
      self.slug = slugify('{} {}'.format(self.profile.title, self.uniqueId))

    self.slug = slugify('{} {}'.format(self.profile.title, self.uniqueId))
    self.last_updated = timezone.localtime(timezone.now())
    super(Project, self).save(*args, **kwargs)



class Rating(models.Model):
  design = models.IntegerField(null=True, blank=True, default=0, validators=[MaxLengthValidator(10), MinLengthValidator(0)])
  usability = models.IntegerField(null=True, blank=True, default=0, validators=[MaxLengthValidator(10), MinLengthValidator(0)])
  content = models.IntegerField(null=True, blank=True, default=0)


  project = models.ForeignKey(Project, null=True, blank=True, on_delete=models.CASCADE)

  uniqueId = models.CharField(null=True, blank=True, max_length=100)
  slug = models.SlugField(max_length=500, unique=True, blank=True, null=True)
  date_created = models.DateTimeField(blank=True, null=True)
  last_updated = models.DateTimeField(blank=True, null=True)

  def __str__(self):
    return '{} {}'.format(self.project.title, self.uniqueId)

  def get_absolute_url(self):
    return reverse('rating-detail', kwargs={'slug': self.slug})

  def save(self, *args, **kwargs):
    if self.date_created is None:
      self.date_created = timezone.localtime(timezone.now())
    if self.uniqueId is None:
      self.uniqueId = str(uuid4()).split('-')[4]
      self.slug = slugify('{} {}'.format(self.project.title, self.uniqueId))

    self.slug = slugify('{} {}'.format(self.project.title, self.uniqueId))
    self.last_updated = timezone.localtime(timezone.now())
    super(Rating, self).save(*args, **kwargs)