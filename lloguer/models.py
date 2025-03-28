from django.db import models
from django.contrib.auth.models import User


class Automobil(models.Model):
    marca = models.CharField(max_length=50)
    model = models.CharField(max_length=50)
    matricula = models.CharField(max_length=10)

    # mostrar en el admin panel correctamente los automobiles
    def __str__(self):
        return f"{self.marca} {self.model} - {self.matricula}"

# Fita 3: crear modelo con FKs y añadir datos via shell
class Reserva(models.Model):
    automobil = models.ForeignKey(Automobil, on_delete=models.CASCADE)
    usuario = models.ForeignKey(User, on_delete=models.CASCADE)
    data_inici = models.DateField()
    data_fi = models.DateField()

    class Meta:
        unique_together = ('automobil', 'data_inici')

    def __str__(self):
        return f"Reserva de {self.automobil} per {self.usuario.username} des de {self.data_inici} fins {self.data_fi}"

# - SHELL -
# from lloguer.models import Automobil, Reserva
# from django.contrib.auth.models import User

# usuario = User.objects.get(username="admin")
# automobil = Automobil.objects.get(matricula="6666 GGG")

# from datetime import date

# reserva = Reserva.objects.create(
#     automobil=automobil,
#     usuario=usuario,
#     data_inici=date(2024, 4, 1),
#     data_fi=date(2024, 4, 5)
# )