from django.db import models

# Create your models here.

class Evento(models.Model):
    nome = models.CharField(max_length=150, blank=True, null=True)
    sigla = models.CharField(max_length=50, blank=True, null=True)
    ano = models.DateField(blank=True, null=True)
    link = models.TextField(blank=True, null=True)

    objects = models.Manager()

    def __str__(self):
        return self.nome