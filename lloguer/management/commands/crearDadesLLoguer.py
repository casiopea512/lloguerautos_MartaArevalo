# Fita 4 - Crear 4 automòbils i 8 usuaris amb 1 o 2 Reserves cadascun - s'ha de poder executar diversos cops seguint sense que falli

from django.core.management.base import BaseCommand
from django.contrib.auth.models import User
from faker import Faker
from random import choice, randint
from lloguer.models import Automobil, Reserva
from datetime import timedelta, date

faker = Faker(["es_CA", "es_ES"])

NUM_AUTOMOIBILS_CREAR = 4
NUM_USUARIS_CREAR = 8
NUM_RESERVES_PER_USUARI = [1,2]

class Command(BaseCommand):
    help = "Crea dades per als lloguers dels automòbils"

    def handle(self, *args, **options):

        # Crear automòbils
        automobils = []
        for i in range(NUM_AUTOMOIBILS_CREAR):
            automobil, created = Automobil.objects.get_or_create(
                matricula=f"{i:03d} ABC",
                defaults={
                    "marca": faker.company(),
                    "model": faker.word(),
                }
            )
            automobils.append(automobil)

            if created:
                print(f"Creat: {automobil.marca} {automobil.model} - {automobil.matricula}")
            else:
                print(f"Tornant a crear l'automòbil perquè ja hi existia")

        # Crear usuaris
        usuaris = []
        for i in range(NUM_USUARIS_CREAR):
            username = f"user{i}"
            user, created = User.objects.get_or_create(
                username=username,
                defaults={"email": faker.email(), "password": "password123"}
            )
            usuaris.append(user)

            if created:
                print(f"Creat: {username.username} - {username.email}")
            else:
                print(f"Tornant a crear l'usuari perquè ja hi existia")
        

        # Crear reserves
        for usuari in usuaris:
            num_reserves = choice(NUM_RESERVES_PER_USUARI)
            for _ in range(num_reserves):
                automobil = choice(automobils)
                data_inici = date.today() + timedelta(days=randint(1, 30))
                data_fi = data_inici + timedelta(days=randint(1, 7))

                
                reserva, created = Reserva.objects.get_or_create(
                    automobil=automobil,
                    data_inici=data_inici,
                    defaults={
                        "usuario": usuari,
                        "data_fi": data_fi
                    }
                )

                if created:
                    print(f"Creat: {reserva.automobil}: {reserva.data_inici} - {reserva.data_fi} ")
                else:
                    print(f"Tornant a crear la reserva perquè ja hi existia")
        
        print("Reserves creades correctament!")