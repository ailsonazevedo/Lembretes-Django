from email.policy import default
from django import forms
from django.db import models
from django.contrib.auth.models import User

class Perfil(models.Model):
    nome = models.CharField(max_length=200)
    email = models.EmailField(max_length=200, null= True)

    def __str__(self):
        return (self.nome)


class Lembrete (models.Model):
    nome = models.CharField(max_length=200)
    descricao = models.CharField(max_length=300)
    data_lembrete = models.DateTimeField(verbose_name='Data do Lembrete', null=True)
    file = models.FileField(upload_to="media/", null=True, blank=True)
    ativo = models.BooleanField(default=False)
    usuario = models.ForeignKey(User,on_delete=models.CASCADE, null=True)
    #perfil = models.ForeignKey(Perfil,on_delete=models.CASCADE, null=True)

    def __str__(self):
        return (self.nome)


# Create your models here.
