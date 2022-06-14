from django.test import TestCase
from .models import Profile,Projects
from django.contrib.auth.models import User

# Create your tests here.

class ProfileTest(TestCase):
    def setUp(self):
        self.martin = User(username = 'Martin',email = 'martin@gmail.com')
        self.martin = Profile(user = Self.martin, User = 1,Bio = 'tests',photo = 'test.jpg',date_craeted='dec,01.2020')

    def test_instance(self):
        self.assertTrue(isinstance(self.martin,Profile))


    def test_save_profile(self):
        Profile.save_profile(self)
        all_profiles = Profile.objects.all()
        self.assertTrue(len(all_profiles),0)

    def test_delete_profile(self):
        self.martin.delete_profile()
        all_profiles = Profile.objects.all()
        self.assertEqual(len(all_profiles),0)