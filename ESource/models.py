from django.db import models

# Create your models here.
class Evento(models.Model):
    class Status(models.TextChoices):
        DISPONIVEL = 'DISP', 'Disponível'
        ARQUIVADO = 'ARQ', 'Arquivado'
    nome = models.CharField(max_length=150, blank=True, null=True)
    sigla = models.CharField(max_length=50, blank=True, null=True)
    data = models.DateField(blank=True, null=True)
    link = models.TextField(blank=True, null=True)
    
    status = models.CharField(
        max_length=4,
        choices=Status.choices,
        default=Status.DISPONIVEL,
    )

    def __str__(self):
        return self.nome

class Artigo(models.Model):
    class Status(models.TextChoices):
        DISPONIVEL = 'DISP', 'Disponível'
        ARQUIVADO = 'ARQ', 'Arquivado'
    titulo = models.CharField(max_length=150, blank=True, null=True)
    subAreas = models.CharField(max_length=150, blank=True, null=True)
    dataPublicacao = models.DateField(blank=True, null=True)
    link = models.TextField(blank=True, null=True)
    conteudo = models.TextField(blank=True, null=True)
    
    status = models.CharField(
        max_length=4,
        choices=Status.choices,
        default=Status.DISPONIVEL,
    )
    
    autores = models.ManyToManyField('Autor', related_name='artigos')

    evento = models.ForeignKey(Evento, on_delete=models.CASCADE, related_name='artigos', blank=True, null=True)

    def __str__(self):
        return self.titulo

class Autor(models.Model):
    nome = models.CharField(max_length=150, blank=True, null=True)
    citacao = models.CharField(max_length=150, blank=True, null=True)
    instituicao = models.CharField(max_length=10, blank=True, null=True)
    unidade_federativa = models.CharField(max_length=10, blank=True, null=True)

    class Meta:
        verbose_name = "Autores"
        verbose_name_plural = "Autores"
        
    def __str__(self):
        return self.nome

class Status(models.Model):
    modelo = models.CharField(max_length=100)  # Ex: 'Artigo', 'Evento'
    objetoId = models.PositiveIntegerField()   # ID do objeto modificado
    atualizado = models.DateTimeField(auto_now=True)

    class Meta:
        unique_together = ('modelo', 'objetoId')
        verbose_name = "Status"
        verbose_name_plural = "Status"

    def __str__(self):
        atualizadoFormatada = self.atualizado.strftime('%d/%m/%Y %H:%M') if self.atualizado else 'Sem data'
        return f"{self.modelo} #{self.objetoId} - {atualizadoFormatada}"