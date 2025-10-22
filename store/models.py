from django.db import models
from django.core.exceptions import ValidationError


class Categoria(models.Model):
    nombre = models.CharField(max_length=100, unique=True)
    descripcion = models.TextField(blank=True, null=True)

    class Meta:
        verbose_name = "Categoría"
        verbose_name_plural = "Categorías"
    
    def __str__(self):
        return self.nombre
class Subcategoria(models.Model):
    categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE, related_name='subcategorias')
    nombre = models.CharField(max_length=100)

    class Meta:
        verbose_name = "Subcategoría"
        verbose_name_plural = "Subcategorías"

    def __str__(self):
        return f"{self.categoria.nombre} → {self.nombre}"

    def __str__(self):
        return self.nombre
   

class Producto(models.Model):
    nombre = models.CharField(max_length=100)
    categoria = models.ForeignKey(Categoria, on_delete=models.SET_NULL, null=True, blank=True)
    subcategoria = models.ForeignKey(Subcategoria, on_delete=models.SET_NULL, null=True, blank=True)
    precio = models.DecimalField(max_digits=10, decimal_places=2)
    cantidad = models.PositiveIntegerField(default=1)
    talla = models.CharField(max_length=10, blank=True, null=True)
    dimensiones = models.CharField(max_length=100, blank=True, null=True)
    descripcion = models.TextField(blank=True, null=True)
    imagen = models.ImageField(upload_to='productos/', blank=True, null=True)
    activo = models.BooleanField(default=True)
    stock = models.PositiveIntegerField(default=20)
    class Meta:
        verbose_name = "Producto"
        verbose_name_plural = "Productos"
 
    def clean(self):
        # 🧩 Validar que el precio no sea negativo
        if self.precio < 0:
            raise ValidationError({'precio': 'El precio no puede ser negativo.'})

        # 🧩 Validar que la cantidad esté entre 1 y el stock
        if self.cantidad <= 0:
            raise ValidationError({'cantidad': 'La cantidad debe ser mayor que 0.'})

        if self.cantidad > self.stock:
            raise ValidationError({'cantidad': 'La cantidad no puede superar el stock disponible.'})

    def save(self, *args, **kwargs):
        # Llama al método clean() antes de guardar
        self.clean()
        super().save(*args, **kwargs)
 
    def __str__(self):
        return f"{self.nombre} - ${self.precio}"

