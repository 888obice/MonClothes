from django.db import models

class Producto(models.Model):
    nombre = models.CharField(max_length=100)
    descripcion = models.TextField(blank=True)
    precio = models.DecimalField(max_digits=10, decimal_places=2)
    imagen = models.ImageField(upload_to='productos/', null=True, blank=True)  # Opcional
    # Agrega campos como talla, color, categoría si los usas en el carrito

    def __str__(self):
        return self.nombre