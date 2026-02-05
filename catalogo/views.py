from django.shortcuts import render
from .models import Sede

# 1. Vista de Inicio (La Portada)
def index(request):
    return render(request, 'index.html')

# 2. Vista de Sedes (El Mapa)
def sedes(request):
    todas_las_sedes = Sede.objects.all()
    return render(request, 'sedes.html', {'sedes': todas_las_sedes})