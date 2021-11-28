from django.contrib.auth.models import Group
from django.db.models import fields
from rest_framework import serializers

from api.models import User, Comentario, Postagem

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ["id", "url", "username", "email", "groups"]


class GroupSerializer(serializers.ModelSerializer):
    class Meta:
        model = Group
        fields = ["id", "url", "name"]


class PostagemSerializer(serializers.ModelSerializer):
    class Meta:
        model = Postagem
        fields = ["id", "created", "autor", "likes", "conteudo"]

class ComentarioSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comentario
        fields = ["id", "created", "autor", "postagem", "conteudo"]

# class ConteudoSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Conteudo
#         fields = [
#             "id", 
#             "created",
#             "postagem",
#             "conteudo",
#             "texto",
#         ]

# class ConteudoMidiaSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = ConteudoMidia
#         fields = [
#             "id", 
#             "created",
#             "nome",
#             "arquivo",
#             "conteudo",
#         ]
