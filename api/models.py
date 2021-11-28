from django.db import models
from django.utils.translation import ugettext_lazy as _
from django.contrib.auth.models import (
    AbstractBaseUser,
    PermissionsMixin,
    Group,
    BaseUserManager,
    UserManager,
)
from django.core import validators
from django.contrib.postgres.fields import ArrayField
from django.utils import timezone
import pytz
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
        default=timezone.now,
    )

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = ["username"]
    objects = UserManager()


class Postagem(models.Model):
    """
    Postagem model
    """

    created = models.DateTimeField(default=timezone.now)
    autor = models.ForeignKey(User, on_delete=models.CASCADE)
    conteudo = models.CharField(max_length=280, default="", null=False)
    likes = models.ManyToManyField(User, related_name="likes", blank=True)

    # override
    def __str__(self) -> str:
        return f"{self.id}"


class Comentario(models.Model):
    """
    Comentario model
    """

    created = models.DateTimeField(default=timezone.now)
    autor = models.ForeignKey(User, on_delete=models.CASCADE)
    postagem = models.ForeignKey(Postagem, on_delete=models.CASCADE)
    conteudo = models.CharField(max_length=280, default="", null=False)

    def __str__(self) -> str:
        return f"{self.autor} - {self.id}"


# class Conteudo(models.Model):
#     """
#     Conteudo model
#     """

#     created = models.DateTimeField(default=timezone.now)
#     postagem = models.ForeignKey(
#         Postagem, blank=True, null=True, on_delete=models.CASCADE
#     )
#     conteudo = models.ForeignKey(
#         Comentario, blank=True, null=True, on_delete=models.CASCADE
#     )
#     texto = models.TextField()

#     def __str__(self) -> str:
#         return f"{self.id} - Postagem: {self.postagem}"


# class ConteudoMidia(models.Model):
#     # TODO definir um local mais adequado para fazer o upload de arquivos
#     created = models.DateTimeField(default=timezone.now)
#     nome = models.CharField(max_length=20, null=True)
#     arquivo = models.FileField(
#         upload_to="files/%Y/%m/%d",
#         blank=True,
#         null=True,
#     )
#     conteudo = models.ForeignKey(
#         Conteudo,
#         on_delete=models.CASCADE,
#         related_name="files",
#     )

#     def __str__(self) -> str:
#         return self.nome + " : " + self.conteudo
