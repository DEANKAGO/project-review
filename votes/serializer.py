from rest_framework import serializers
from .models import Profile,Projects, Review

class ProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profile
        fields = ('Bio', 'photo', 'user')


class ProjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = Projects
        fields = ('title', 'description', 'projects_screenshot','project_url','user')  



class ReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = Review
        fields = ('id', 'design', 'usability', 'content')
        