from django.contrib import admin
from .models import Automobil, Reserva

# Registrar Automobil con su configuración personalizada
class AutomobilAdmin(admin.ModelAdmin):
    list_display = ('marca', 'model', 'matricula')  

# Registrar Reserva con su configuración personalizada
class ReservaAdmin(admin.ModelAdmin):
    list_display = ('automobil', 'usuario', 'data_inici', 'data_fi')

admin.site.register(Automobil)
admin.site.register(Reserva)