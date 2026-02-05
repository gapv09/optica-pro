from django.db import models

# 1. Modelo de Categoría
class Categoria(models.Model):
    nombre = models.CharField(max_length=50) # Ej: "Sol", "Medida", "Niños"
    
    def __str__(self):
        return self.nombre

# 2. Modelo de Producto
class Producto(models.Model):
    nombre = models.CharField(max_length=200) # Ej: Ray-Ban Aviator Classic
    categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE)
    descripcion = models.TextField()
    precio = models.DecimalField(max_digits=10, decimal_places=2) # 350.00
    stock = models.IntegerField(default=10)
    imagen = models.ImageField(upload_to='productos/', null=True, blank=True)
    activo = models.BooleanField(default=True)

    def __str__(self):
        return self.nombre

# 3. Modelo de Sede (El nuevo)
class Sede(models.Model):
    nombre = models.CharField(max_length=100)  # Ej: Villasol
    direccion = models.CharField(max_length=200, blank=True)
    latitud = models.FloatField()
    longitud = models.FloatField()
    horario = models.CharField(max_length=100, default="Lunes a Sábado: 9am - 8pm")
    
    def __str__(self):
        return self.nombre