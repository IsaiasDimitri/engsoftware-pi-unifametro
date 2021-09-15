from django.db import models

# Create your models here.

# class Conteudo(models.Model):
#     created = models.DateTimeField(auto_now_add=True)
#     title = models.CharField(max_length=100, blank=True, default='')


# class Comentario(models.Model):
#     created = models.DateTimeField(auto_now_add=True)
#     popularity = models.IntegerField(default=0)
#     content = models.OneToOneField(
#         Conteudo,
#         on_delete=models.CASCADE
#     )

# class Postagem(models.Model):
#     created = models.DateTimeField(auto_now_add=True)
#     popularity = models.IntegerField(default=0)
#     content = models.OneToOneField(
#         Conteudo,
#         on_delete=models.CASCADE
#     )
#     class Meta:
#         ordering = ['created']
