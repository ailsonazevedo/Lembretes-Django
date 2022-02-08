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
    nome = models.CharField(max_length=180)
    descricao = models.CharField(verbose_name='Descrição',max_length=300, blank=True)
    data_lembrete = models.DateTimeField(verbose_name='Data do Lembrete', null=True)
    data_criacao = models.DateTimeField('Data de Criação', auto_now_add=True, null=True, editable=False)
    file = models.FileField(upload_to="media/", null=True, blank=True)
    concluido = models.BooleanField('Concluído',default=False)
    usuario = models.ForeignKey(User,on_delete=models.CASCADE, null=True)
    #perfil = models.ForeignKey(Perfil,on_delete=models.CASCADE, null=True)

    class Meta:
        db_table = 'lembrete'


    def __str__(self):
        return (self.nome)


# Create your models here.
