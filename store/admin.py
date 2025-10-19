from django.contrib import admin
from .models import Categoria, Subcategoria, Producto

@admin.register(Categoria)
class CategoriaAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'descripcion')
    search_fields = ('nombre',)

@admin.register(Subcategoria)
class SubcategoriaAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'categoria')
    list_filter = ('categoria',)
    search_fields = ('nombre',)

@admin.register(Producto)
class ProductoAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'categoria', 'subcategoria', 'precio', 'cantidad', 'activo')
    list_filter = ('categoria', 'subcategoria', 'activo')
    search_fields = ('nombre',)
    list_editable = ('precio', 'cantidad', 'activo')


