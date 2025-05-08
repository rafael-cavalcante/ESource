from django.db import models

# Create your models here.

class Evento(models.Model):
    nome = models.CharField(max_length=150, blank=True, null=True)
    sigla = models.CharField(max_length=50, blank=True, null=True)
    data = models.DateField(blank=True, null=True)
    link = models.TextField(blank=True, null=True)

    objects = models.Manager()

    def __str__(self):
        return self.nome

class Artigo(models.Model):
    titulo = models.CharField(max_length=150, blank=True, null=True)
    autor = models.CharField(max_length=150, blank=True, null=True)
    subAreas = models.CharField(max_length=150, blank=True, null=True)
    dataPublicacao = models.DateField(blank=True, null=True)
    link = models.TextField(blank=True, null=True)
    imagem = models.TextField(blank=True, null=True)
    conteudo = models.TextField(blank=True, null=True)

    evento = models.ForeignKey(Evento, on_delete=models.CASCADE, related_name='artigos', blank=True, null=True)

    objects = models.Manager()

    def __str__(self):
        return self.titulo

