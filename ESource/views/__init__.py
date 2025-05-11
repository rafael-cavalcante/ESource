from .views_artigo import artigos, criar_artigo, exibir_artigo, editar_artigo, excluir_artigo, arquivar_artigo, desarquivar_artigo, listar_artigos_arquivados
from .views_evento import eventos, cadastrarEvento, atualizarEvento, deletarEvento, arquivar_evento, desarquivar_evento, listar_eventos_arquivados
from .views_autor import autores, cadastrarAutor, atualizarAutor, deletarAutor
from .views_usuario import entrar, sair

__all__ = [
    'artigos',
    'criar_artigo',
    'exibir_artigo',
    'editar_artigo',
    'excluir_artigo',
    'arquivar_artigo',
    'desarquivar_artigo',
    'listar_artigos_arquivados',
    
    'eventos',
    'cadastrarEvento',
    'atualizarEvento',
    'deletarEvento',
    'arquivar_evento',
    'desarquivar_evento',
    'listar_eventos_arquivados',
    
    'autores',
    'cadastrarAutor', 
    'atualizarAutor',
    'deletarAutor',
    
    'entrar',
    'sair',
]