from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from django.contrib.auth.models import User
from .models import Producto, Sede, Categoria

# 1. VISTA DE INICIO (Portada)
def index(request):
    return render(request, 'index.html')

# 2. VISTA DE SEDES (Mapa)
def sedes(request):
    todas_las_sedes = Sede.objects.all()
    return render(request, 'sedes.html', {'sedes': todas_las_sedes})

# 3. VISTA DEL CATÁLOGO (Con Filtros)
def catalogo(request):
    productos = Producto.objects.filter(activo=True)
    
    # Lógica de Filtros
    material_filter = request.GET.get('material')
    color_filter = request.GET.get('color')
    
    if material_filter:
        productos = productos.filter(material=material_filter)
    if color_filter:
        productos = productos.filter(color=color_filter)
        
    context = {
        'productos': productos,
        'colores': Producto.COLORES,
        'materiales': Producto.MATERIALES
    }
    return render(request, 'catalogo.html', context)

# 4. VISTA DE DETALLE (Producto Individual)
def detalle_producto(request, producto_id):
    producto = get_object_or_404(Producto, pk=producto_id)
    return render(request, 'detalle.html', {'producto': producto})

# 5. CONFIGURACIÓN AUTOMÁTICA (Setup Secreto)
def setup_datos(request):
    # Crear Superusuario
    if not User.objects.filter(username='admin').exists():
        User.objects.create_superuser('admin', 'tu_correo@gmail.com', 'Admin1234')
        mensaje_user = "✅ Usuario 'admin' creado (Contraseña: Admin1234)<br>"
    else:
        mensaje_user = "ℹ️ El usuario 'admin' ya existía.<br>"

    # Crear Sedes
    if Sede.objects.count() == 0:
        Sede.objects.create(nombre="Villasol", latitud=-11.95927375686443, longitud=-77.07330486248584, direccion="Av. Universitaria, Villasol")
        Sede.objects.create(nombre="Santo Domingo", latitud=-11.884652507861606, longitud=-77.03474940666565, direccion="Urb. Santo Domingo")
        Sede.objects.create(nombre="Comas", latitud=-11.930960920593678, longitud=-77.05457383365076, direccion="Av. Túpac Amaru, Comas")
        Sede.objects.create(nombre="Huandoy", latitud=-11.975919500643759, longitud=-77.08277603364986, direccion="Ovalo Huandoy")
        mensaje_sedes = "✅ Las 4 sedes fueron creadas exitosamente."
    else:
        mensaje_sedes = "ℹ️ Las sedes ya existían."

    return HttpResponse(mensaje_user + mensaje_sedes)