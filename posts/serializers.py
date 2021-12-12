from django.contrib.auth.models import User, Group
from django_celery_beat.models import PeriodicTask
from .models import Post
from rest_framework import serializers

class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ('url', 'username', 'email', 'groups')

class GroupSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Group
        fields = ('url', 'name')

class PeriodicTaskSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = PeriodicTask
        fields = ('interval', 'name', 'task', 'args')

class PostSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Post
        fields = ('id', 'platform', 'user', 'link', 'created_at', 'text', 'title')
