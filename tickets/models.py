from django.conf import settings
from django.db import models


class Ticket(models.Model):
    class Estado(models.TextChoices):
        ABIERTO = 'abierto', 'Abierto'
        EN_PROCESO = 'en_proceso', 'En proceso'
        CERRADO = 'cerrado', 'Cerrado'

    class Prioridad(models.TextChoices):
        BAJA = 'baja', 'Baja'
        MEDIA = 'media', 'Media'
        ALTA = 'alta', 'Alta'

    titulo = models.CharField(max_length=120)
    descripcion = models.TextField()
    estado = models.CharField(max_length=20, choices=Estado.choices, default=Estado.ABIERTO)
    prioridad = models.CharField(max_length=10, choices=Prioridad.choices, default=Prioridad.MEDIA)
    creado_por = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='tickets')
    creado_en = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-creado_en']

    def __str__(self):
        return f'{self.titulo} ({self.get_estado_display()})'