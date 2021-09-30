from django.contrib.auth.models import User, Group
from django.db.models import fields
from rest_framework import serializers

from api.models import Postagem

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['url', 'username', 'email', 'groups']


class GroupSerializer(serializers.ModelSerializer):
    class Meta:
        model = Group
        fields = ['url', 'name']

class PostagemSerializer(serializers.ModelSerializer):
    class Meta:
        model = Postagem
        fields = ['create', 'autor', 'grupo', 'titulo', 'likes']