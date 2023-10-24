from django.contrib import admin
from .models import Entidad, Comunicado
from django.core.exceptions import PermissionDenied

class validacion(admin.ModelAdmin):
    list_display = ("id", "titulo", "publicado_por","modificado_por", "tipo", "fecha_publicacion", "visible")

    def save_model(self, request, obj, form, change):

        if not change:
            obj.publicado_por = request.user
        
        super().save_model(request, obj, form, change)

admin.site.register(Entidad)
admin.site.register(Comunicado, validacion)