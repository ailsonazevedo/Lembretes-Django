from django.db import models

class Lembrete (models.Model):
    nome = models.CharField(max_length=200)
    descricao = models.CharField(max_length=300)
    file = models.FileField(upload_to="media/", null=True, blank=True)



    def __str__(self):
        return (self.nome)

class Perfil(models.Model):
    nome = models.CharField(max_length=200)
    email = models.CharField(max_length=200, null= True)




# Create your models here.
