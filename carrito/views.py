from django.shortcuts import redirect, render, get_object_or_404
from store.models import Producto
from .carrito import Carrito
from django.http import JsonResponse
from django.template.loader import render_to_string


def agregar_al_carrito(request, producto_id):
    carrito = Carrito(request)
    producto = get_object_or_404(Producto, id=producto_id)
    carrito.agregar(producto)
    return redirect("catalogo")

def eliminar_del_carrito(request, producto_id):
    carrito = Carrito(request)
    producto = get_object_or_404(Producto, id=producto_id)
    carrito.eliminar(producto)
    return redirect("ver_carrito")

def restar_del_carrito(request, producto_id):
    carrito = Carrito(request)
    producto = get_object_or_404(Producto, id=producto_id)
    carrito.restar(producto)
    return redirect("ver_carrito")

def limpiar_carrito(request):
    carrito = Carrito(request)
    carrito.limpiar()
    return redirect("catalogo")

def ver_carrito(request):
    carrito = Carrito(request)
    contexto = {
        "carrito": carrito.carrito,
        "total": carrito.total(),
    }
    return render(request, "carrito/ver_carrito.html", contexto)

def vista_carrito_ajax(request):
    from django.http import JsonResponse
    from django.template.loader import render_to_string
    from .carrito import Carrito
    carrito = Carrito(request)
    html = render_to_string("carrito/_mini_carrito.html", {
        "carrito": carrito.carrito,
        "total": carrito.total(),
    }, request=request)
    return JsonResponse({"html": html})
