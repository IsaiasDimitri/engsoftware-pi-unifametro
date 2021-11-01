from django.contrib.auth.models import User, Group
from django.db.models import fields
from rest_framework import serializers

from api.models import Comentario, Conteudo, ConteudoMidia, Postagem


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ["url", "username", "email", "groups"]


class GroupSerializer(serializers.ModelSerializer):
    class Meta:
        model = Group
        fields = ["url", "name"]


class PostagemSerializer(serializers.ModelSerializer):
    class Meta:
        model = Postagem
        fields = ["created", "autor", "grupo", "titulo", "likes"]

class ComentarioSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comentario
        fields = ["created", "autor"]

class ConteudoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Conteudo
        fields = [
            "created",
            "postagem",
            "conteudo",
            "texto",
            "imagens",
            "arquivos",
        ]

class ConteudoMidiaSerializer(serializers.ModelSerializer):
    class Meta:
        model = ConteudoMidia
        fields = [
            "created",
            "nome",
            "arquivo",
            "conteudo",
        ]
