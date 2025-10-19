from django.shortcuts import redirect, render
from store.models import Producto
from .carrito import Carrito

def agregar_producto(request, producto_id):
    carrito = Carrito(request)
    producto = Producto.objects.get(id=producto_id)
    carrito.agregar(producto)
    return redirect('tienda')

def eliminar_producto(request, producto_id):
    carrito = Carrito(request)
    producto = Producto.objects.get(id=producto_id)
    carrito.eliminar(producto)
    return redirect('tienda')

def restar_producto(request, producto_id):
    carrito = Carrito(request)
    producto = Producto.objects.get(id=producto_id)
    carrito.restar(producto)
    return redirect('tienda')

def limpiar_carrito(request):
    carrito = Carrito(request)
    carrito.limpiar()
    return redirect('tienda')

def ver_carrito(request):
        carrito = Carrito(request)
        items = []
        total = 0
        for item_id, item in carrito.carrito.items():
            try:
                producto = Producto.objects.get(id=item_id)
                subtotal = producto.precio * item['cantidad']
                items.append({
                    'producto': producto,
                    'cantidad': item['cantidad'],
                    'subtotal': subtotal
                })
                total += subtotal
            except Producto.DoesNotExist:
                pass
        return render(request, 'carrito/ver_carrito.html', {'items': items, 'total': total})
