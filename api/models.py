from django.db import models
from django.utils.translation import ugettext_lazy as _
from django.contrib.auth.models import (
    AbstractBaseUser,
    PermissionsMixin,
    Group,
    BaseUserManager
)
from django.core import validators
from django.contrib.postgres.fields import ArrayField
from datetime import datetime
import re

# Create your models here.


class User(AbstractBaseUser, PermissionsMixin):
    """
    User model
    """

    username = models.CharField(
        _("username"),
        max_length=15,
        unique=True,
        help_text=_(
            "Required. 15 characters or fewer. Letters, numbers and @/./+/-/_ characters"
        ),
        validators=[
            validators.RegexValidator(
                re.compile("^[\w.@+-]+$"),
                _("Enter a valid username."),
                _("invalid"),
            ),
        ],
    )
    first_name = models.CharField(
        _("first name"),
        max_length=30,
    )
    last_name = models.CharField(
        _("last name"),
        max_length=30,
    )
    email = models.EmailField(
        _("email address"),
        max_length=255,
        unique=True,
    )
    is_staff = models.BooleanField(
        _("staff status"),
        default=False,
        help_text=_("Designates whether the user can log into this admin site."),
    )
    is_active = models.BooleanField(
        _("active"),
        default=True,
        help_text=_(
            "Designates whether this user should be treated as active. Unselect this instead of deleting accounts."
        ),
    )
    date_joined = models.DateTimeField(
        _("date joined"),
        default=datetime.now,
    )

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = ["username"]


class Postagem(models.Model):
    """
    Postagem model
    """

    created = models.DateTimeField(default=datetime.now)
    autor = models.ForeignKey(User, on_delete=models.CASCADE)
    grupo = models.ForeignKey(Group, default=None, on_delete=models.SET_DEFAULT)
    titulo = models.CharField(max_length=45, default="", null=False)
    likes = ArrayField(models.IntegerField(), null=True)

    # override
    def __str__(self) -> str:
        return f"Autor: {self.autor}"


class Comentario(models.Model):
    """
    Comentario
    """

    created = models.DateTimeField(default=datetime.now)
    autor = models.ForeignKey(User, on_delete=models.CASCADE)


class Conteudo(models.Model):
    """
    Conteudo model
    """

    created = models.DateTimeField(default=datetime.now)
    postagem = models.ForeignKey(Postagem, null=True, on_delete=models.CASCADE)
    conteudo = models.ForeignKey(Comentario, null=True, on_delete=models.CASCADE)
    texto = models.TextField()
    # lista de imagens
    imagens = ArrayField(
        models.ImageField(upload_to="uploads/img/%Y/%m/%d/"),
        size=3,
        null=True,
    )
    # lista de arquivos
    arquivos = ArrayField(
        models.FileField(upload_to="uploads/files/%Y/%m/%d/"),
        size=3,
        null=True,
    )

    def __str__(self) -> str:
        return super().__str__()
