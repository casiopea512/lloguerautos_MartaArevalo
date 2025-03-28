from django.shortcuts import render
from .models import Automobil

# Create your views here.
def llista_automobils(request):
    automobils = Automobil.objects.all().prefetch_related("reserva_set")
    return render(request, "lloguer/llista_automobils.html", {"automobils": automobils})