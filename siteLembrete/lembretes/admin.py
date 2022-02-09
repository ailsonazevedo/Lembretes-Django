from django.contrib import admin
from .models import *


@admin.register(Lembrete)

class LembreteAdmin(admin.ModelAdmin):
    list_display = ('nome','descricao' ,'data_lembrete', 'data_criacao', 'concluido')
    list_filter = (('concluido', admin.BooleanFieldListFilter),('nome'),('data_criacao'),('data_lembrete'))

# Register your models here.

admin.site.register(Perfil)
#admin.site.register(LembreteAdmin)
