from django.contrib import admin
from .models import *


@admin.register(Lembrete)

class LembreteAdmin(admin.ModelAdmin):
    list_display = ('nome','descricao' ,'data_lembrete', 'data_criacao', 'concluido')
    #list_filter = ('data_lembrete', 'data-criacao')

# Register your models here.

admin.site.register(Perfil)
#admin.site.register(LembreteAdmin)
