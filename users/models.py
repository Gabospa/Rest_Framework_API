from django.db import models

class Persona(models.Model):
    id = models.AutoField(primary_key = True)
    first_name = models.CharField('Nombre', max_length=100)
    last_name = models.CharField('Apellido', max_length=100)
    username = models.CharField('Usuario', max_length=100)
    email = models.EmailField()
    password = models.CharField(max_length=100)
    birthdate = models.DateField()

    def __str__(self):
        return self.username
