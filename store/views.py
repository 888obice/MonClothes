# store/views.py (fragmento sugerido)

from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.db.models import Q
from django.shortcuts import render
from .models import Producto, Categoria


def index(request):
    productos = Producto.objects.all()
    categorias = Categoria.objects.all()
    return render(request, "store/index.html", {
        "productos": productos,
        "categorias": categorias,
    })

def tienda(request):
    productos = Producto.objects.filter(activo=True)
    return render(request, "store/tienda.html", {"productos": productos})

def catalogo(request):
    categorias = Categoria.objects.all()
    productos = Producto.objects.filter(activo=True)
    return render(request, "store/catalogo.html", {
        "categorias": categorias,
        "productos": productos
    })

@csrf_exempt
def buscar_productos(request):
    termino = request.GET.get("q", "").strip().lower()
    resultados = []
    SINONIMOS = {
        "chaleco": ["polerón", "abrigo", "suéter", "parka"],
        "polera": ["camiseta", "top", "blusa"],
        "falda": ["minifalda", "pollera"],
        "pantalón": ["jean", "pantalones", "jogger"],
        "zapatillas": ["tenis", "botines", "zapatos"],
    }

    if not termino:
        # si no se escribió nada, mostrar catálogo completo
        productos = Producto.objects.all()
    else:
        palabras = [termino] + SINONIMOS.get(termino, [])
        filtro = Q()
        for palabra in palabras:
            filtro |= Q(nombre__icontains=palabra)
        productos = Producto.objects.filter(filtro)

    # Si la petición es AJAX (desde fetch), devolvemos JSON
    if request.headers.get("x-requested-with") == "XMLHttpRequest":
        for p in productos[:8]:  # máx. 8 para el popup
            resultados.append({
                "id": p.id,
                "nombre": p.nombre,
                "precio": float(p.precio),
                "imagen": p.imagen.url if p.imagen else "",
            })
        return JsonResponse({"resultados": resultados})

    # Si no es AJAX (Enter presionado), renderizamos una página completa
    categorias = Categoria.objects.all()
    return render(request, "store/resultados_busqueda.html", {
        "productos": productos,
        "termino": termino,
        "categorias": categorias,
    })