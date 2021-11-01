from django.contrib import admin

from api import models

# Register your models here.
admin.site.register(models.User)
admin.site.register(models.Comentario)
admin.site.register(models.Postagem)
admin.site.register(models.Conteudo)
admin.site.register(models.ConteudoMidia)