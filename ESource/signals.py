from .models import Evento, Artigo, Autor, Status
from django.db.models.signals import post_save
from django.dispatch import receiver

def atualizar_status(instance):
    Status.objects.update_or_create(
        modelo=instance.__class__.__name__,
        objetoId=instance.id,
        defaults={'atualizado': instance.updated_at if hasattr(instance, 'updated_at') else None}
    )

@receiver(post_save, sender=Artigo)
def registrar_alteracao_artigo(sender, instance, **kwargs):
    atualizar_status(instance)

@receiver(post_save, sender=Evento)
def registrar_alteracao_evento(sender, instance, **kwargs):
    atualizar_status(instance)
    
@receiver(post_save, sender=Autor)
def registrar_alteracao_autor(sender, instance, **kwargs):
    atualizar_status(instance)