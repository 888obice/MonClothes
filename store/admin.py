from django.contrib import admin
from .models import Categoria, Subcategoria, Producto, Marca


@admin.register(Categoria)
class CategoriaAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'descripcion')
    search_fields = ('nombre',)
    ordering = ('nombre',)


@admin.register(Subcategoria)
class SubcategoriaAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'categoria')
    search_fields = ('nombre',)
    list_filter = ('categoria',)
    ordering = ('categoria', 'nombre')


@admin.register(Producto)
class ProductoAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'precio', 'categoria', 'activo', 'fecha_creacion')
    list_editable = ('activo',)
    search_fields = ('nombre', 'categoria__nombre')
    list_filter = ('categoria', 'activo')
    ordering = ('-fecha_creacion',)


@admin.register(Marca)
class MarcaAdmin(admin.ModelAdmin):
    list_display = ('nombre',)
    search_fields = ('nombre',)
