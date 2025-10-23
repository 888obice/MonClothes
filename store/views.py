from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .models import Producto, Categoria

@login_required
def inicio(request):
    return render(request, 'inicio.html')

def index (request):
    return render(request,'index.html')

def tienda(request):
    productos = Producto.objects.all()
    return render(request, 'store/tienda.html', {'productos': productos})

def catalogo(request):
    categorias = Categoria.objects.all().prefetch_related('subcategorias')
    productos = Producto.objects.filter(activo=True)
    return render(request, 'store/catalogo.html', {
        'categorias': categorias,
        'productos': productos
    })
def inicio(request):
    productos = Producto.objects.all()
    return render(request, 'store/index.html', {'productos': productos})
def busqueda(request):
    q = request.GET.get('q', '')
    productos = Producto.objects.filter(nombre__icontains=q)
    if request.headers.get('x-requested-with') == 'XMLHttpRequest':
        return render(request, 'productos_list.html', {'productos': productos})
    return render(request, 'index.html', {'productos': productos})
