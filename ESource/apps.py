from django.apps import AppConfig


class ESourceConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'ESource'
    
    def ready(self):
        import ESource.signals
