from store.models import Producto

class Carrito:
    def __init__(self, request):
        self.session = request.session
        carrito = self.session.get('carrito')
        if not carrito:
            carrito = self.session['carrito'] = {}
        self.carrito = carrito

    def agregar(self, producto):
        id = str(producto.id)
        if id not in self.carrito.keys():
            self.carrito[id] = {
                'producto_id': producto.id,
                'nombre': producto.nombre,
                'precio': str(producto.precio),
                'cantidad': 1,
                'imagen': producto.imagen.url if producto.imagen else '',
            }
        else:
            self.carrito[id]['cantidad'] += 1
        self.guardar()

    def eliminar(self, producto):
        id = str(producto.id)
        if id in self.carrito:
            del self.carrito[id]
            self.guardar()

    def restar(self, producto):
        id = str(producto.id)
        if id in self.carrito.keys():
            self.carrito[id]['cantidad'] -= 1
            if self.carrito[id]['cantidad'] <= 0:
                self.eliminar(producto)
            self.guardar()

    def limpiar(self):
        self.session['carrito'] = {}
        self.session.modified = True

    def guardar(self):
        self.session['carrito'] = self.carrito
        self.session.modified = True

    def total(self):
        return sum(int(item['precio']) * item['cantidad'] for item in self.carrito.values())
