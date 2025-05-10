from django.contrib import admin
from .models import Evento, Artigo, Status
# Register your models here.

admin.site.register(Evento)
admin.site.register(Artigo)
admin.site.register(Status)
