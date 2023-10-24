from django.db import models
from django.contrib.auth.models import User

class Entidad(models.Model):
    id = models.BigAutoField(primary_key=True)
    nombre = models.CharField(max_length=50)
    logo = models.ImageField(upload_to='logos', null=True, blank=True)

    def __str__(self) -> str:
        return self.nombre
    
class Comunicado(models.Model):
    id = models.BigAutoField(primary_key=True)
    titulo = models.CharField(max_length=50)
    detalle = models.CharField(max_length=500)
    detalle_corto = models.CharField(max_length=50)
    TIPO_CHOICES = [
        ('S', 'Suspensión de actividades'),
        ('C', 'Suspensión de clase'),
        ('I', 'Información')
    ]
    tipo = models.CharField(max_length=1, choices=TIPO_CHOICES)
    entidad = models.ForeignKey(Entidad, on_delete=models.CASCADE)
    visible = models.BooleanField(default=True)
    fecha_publicacion = models.DateTimeField(auto_now_add=True)
    fecha_ultima_modificacion = models.DateTimeField(auto_now=True)
    publicado_por = models.ForeignKey(User, on_delete=models.CASCADE, editable=False, null=True)
    modificado_por = models.ForeignKey(User, related_name='modificado_por', on_delete=models.CASCADE, editable=False, null=True)

    def __str__(self) -> str:
        return self.titulo