from django.contrib import admin
from .models import *


#class LembreteAdmin(admin.ModelAdmin):
#    list_display = ('nome', 'data_lembrete', 'descricao')
#   list_filter = ('data_lembrete')

# Register your models here.
admin.site.register(Lembrete)
admin.site.register(Perfil)

