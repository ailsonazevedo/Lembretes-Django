from django.shortcuts import render


from .models import *

# Create your views here.
def home(request):
    lembrete = Lembrete.objects.all()
#
    lembrete = {

        'lembrete': lembrete
    }

    return render(request, "home.html", lembrete)
