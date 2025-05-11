from ESource.models import Artigo, Evento, Autor, Status

def get_context_data(extra_context=None):
    context = {
        'totalArtigos': Artigo.objects.filter(status='DISP').count(),
        'totalEventos': Evento.objects.filter(status='DISP').count(),
        'totalAutores': Autor.objects.count(),
        'statusEvento': Status.objects.filter(modelo='Evento').order_by('-atualizado').first(),
        'statusArtigo': Status.objects.filter(modelo='Artigo').order_by('-atualizado').first(),
        'statusAutor': Status.objects.filter(modelo='Autor').order_by('-atualizado').first(),
    }
    if extra_context:
        context.update(extra_context)
    return context
