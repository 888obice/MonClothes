from django.db import models

# ---------------------------------------------------------
# CATEGORÍA PRINCIPAL
# ---------------------------------------------------------
class Categoria(models.Model):
    nombre = models.CharField(max_length=100, unique=True)
    descripcion = models.TextField(blank=True, null=True)

    class Meta:
        verbose_name = "Categoría"
        verbose_name_plural = "Categorías"

    def __str__(self):
        return self.nombre


# ---------------------------------------------------------
# SUBCATEGORÍA
# ---------------------------------------------------------
class Subcategoria(models.Model):
    categoria = models.ForeignKey(
        Categoria,
        on_delete=models.CASCADE,
        related_name='subcategorias'
    )
    nombre = models.CharField(max_length=100, unique=True)

    class Meta:
        verbose_name = "Subcategoría"
        verbose_name_plural = "Subcategorías"

    def __str__(self):
        return f"{self.categoria.nombre} → {self.nombre}"


# ---------------------------------------------------------
# PRODUCTO
# ---------------------------------------------------------
class Producto(models.Model):
    nombre = models.CharField(max_length=200)
    descripcion = models.TextField(blank=True, null=True)
    precio = models.DecimalField(max_digits=10, decimal_places=2)
    imagen = models.ImageField(upload_to='productos/', blank=True, null=True)
    categoria = models.ForeignKey(
        Categoria,
        on_delete=models.SET_NULL,
        null=True,
        related_name='productos'
    )
    subcategoria = models.ForeignKey(
        Subcategoria,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name='productos'
    )
    activo = models.BooleanField(default=True)
    fecha_creacion = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = "Producto"
        verbose_name_plural = "Productos"
        ordering = ['-fecha_creacion']

    def __str__(self):
        return f"{self.nombre} - ${self.precio}"


# ---------------------------------------------------------
# OPCIONAL: MARCA
# ---------------------------------------------------------
class Marca(models.Model):
    nombre = models.CharField(max_length=100, unique=True)

    class Meta:
        verbose_name = "Marca"
        verbose_name_plural = "Marcas"

    def __str__(self):
        return self.nombre
