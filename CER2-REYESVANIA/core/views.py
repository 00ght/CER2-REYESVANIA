from django.shortcuts import render
from core import models

# Create your views here.
def index(request):
    title = "Inicio"
    entidades = models.Entidad.objects.all()
    comunicados = models.Comunicado.objects.filter(visible=True).order_by('-fecha_publicacion')

    data = {
        'title': title,
        'comunicados': comunicados,
        'entidades': entidades
    }
    return render(request, 'core/base.html', data)


