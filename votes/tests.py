from django.test import TestCase
from .models import *
from django.contrib.auth.models import User

# Create your tests here.

class ProfileTest(TestCase):
    def setUp(self):
        self.admin = User(username = 'admin',email = 'martin@gmail.com')
        self.admin = Profile(user = Self.admin, User = 1,Bio = 'profileTests',photo = 'cul6.jpg',date_created='june,14.2022')

    def test_instance(self):
        self.assertTrue(isinstance(self.admin,Profile))


    def test_save_profile(self):
        Profile.save_profile(self)
        all_profiles = Profile.objects.all()
        self.assertTrue(len(all_profiles),0)

    def test_delete_profile(self):
        self.admin.delete_profile()
        all_profiles = Profile.objects.all()
        self.assertEqual(len(all_profiles),0)


class ProjectsTestCase(TestCase):
    def setUp(self):
        self.new_post = Projects(title = 'projectTest',projects_screenshot = 'cul6.jpg',description = 'projectTests',user = admin,project_url = 'https://facebook.com',date_created='june,14.2022')

    def test_save_project(self):
        self.new_post.save_project()
        pictures = Image.objects.all()
        self.assertEqual(len(pictures),1)

    def test_delete_project(self):
        self.new_post.delete_project()
        pictures = Projects.objects.all()
        self.assertEqual(len(pictures),1)  