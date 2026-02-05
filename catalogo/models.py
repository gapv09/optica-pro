# catalogo/models.py
from django.db import models

class Categoria(models.Model):
    nombre = models.CharField(max_length=50)
    def __str__(self): return self.nombre

class Producto(models.Model):
    # Opciones para listas desplegables (Tuplas: Valor BD, Valor Legible)
    MATERIALES = [
        ('acetato', 'Acetato'),
        ('metal', 'Metal'),
        ('titanio', 'Titanio'),
        ('mixto', 'Mixto (Acetato/Metal)'),
    ]
    
    COLORES = [
        ('negro', 'Negro'),
        ('havana', 'Havana (Carey)'),
        ('transparente', 'Transparente'),
        ('dorado', 'Dorado'),
        ('plateado', 'Plateado'),
        ('azul', 'Azul'),
    ]

    nombre = models.CharField(max_length=200)
    categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE)
    marca = models.CharField(max_length=100, default="San Agustín") # Nuevo
    material = models.CharField(max_length=50, choices=MATERIALES, default='acetato') # Nuevo
    color = models.CharField(max_length=50, choices=COLORES, default='negro') # Nuevo
    descripcion = models.TextField()
    precio = models.DecimalField(max_digits=10, decimal_places=2)
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