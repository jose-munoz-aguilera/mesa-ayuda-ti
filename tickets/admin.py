from django.contrib import admin
from .models import Ticket


@admin.register(Ticket)
class TicketAdmin(admin.ModelAdmin):
    list_display = ('titulo', 'estado', 'prioridad', 'creado_por', 'creado_en')
    list_filter = ('estado', 'prioridad')
    search_fields = ('titulo', 'descripcion')