from dataclasses import fields
from tkinter import Widget
from django.forms import ModelForm
from django import forms
from .models import *

class LembreteForm(forms.ModelForm):
    class meta:
        model = Lembrete
        #fields = "__all__"

        fields = ['nome', 'descricao']
        widgets = {

            'nome': forms.TextInput(attrs={'class':'form-control'}),
            'descricao': forms.TextInput(attrs={'class':'form-control'})
        }