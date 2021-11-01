from django.contrib.auth import models
from django.contrib.auth.models import Group
from rest_framework import viewsets
from .serializers import (
    ComentarioSerializer,
    ConteudoMidiaSerializer,
    ConteudoSerializer,
    PostagemSerializer,
    UserSerializer,
    GroupSerializer,
)
from .models import ConteudoMidia, User, Postagem, Conteudo, Comentario


class UserViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """

    queryset = User.objects.all().order_by("-date_joined")
    serializer_class = UserSerializer
    # permission_classes = [permissions.IsAuthenticated]


class GroupViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """

    queryset = Group.objects.all()
    serializer_class = GroupSerializer
    # permission_classes = [permissions.IsAuthenticated]


class PostagemViewSet(viewsets.ModelViewSet):
    queryset = Postagem.objects.all()
    serializer_class = PostagemSerializer

class ComentarioViewSet(viewsets.ModelViewSet):
    queryset = Comentario.objects.all()
    serializer_class = ComentarioSerializer

class ConteudoViewSet(viewsets.ModelViewSet):
    queryset = Conteudo.objects.all()
    serializer_class = ConteudoSerializer

class ConteudoMidiaViewSet(viewsets.ModelViewSet):
    queryset = ConteudoMidia.objects.all()
    serializer_class = ConteudoMidiaSerializer