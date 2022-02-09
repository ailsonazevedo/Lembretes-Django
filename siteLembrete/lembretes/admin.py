from re import search
from django.contrib import admin
from .models import *
from django.contrib import *


@admin.register(Lembrete)

class LembreteAdmin(admin.ModelAdmin):
    list_display = ('nome','descricao' ,'data_lembrete', 'data_criacao', 'concluido')
    list_filter = (('concluido', admin.BooleanFieldListFilter),('nome'),('data_criacao'),('data_lembrete'))
    search_fields = (('name'),)



# Register your models here.

admin.site.register(Perfil)
#admin.site.register(LembreteAdmin)
