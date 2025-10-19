from django.shortcuts import render
from django.db.models import Q
from store.models import Producto
from .forms import BusquedaForm

def busqueda(request):
        form = BusquedaForm(request.GET or None)
        resultados = Producto.objects.none()

        if form.is_valid():
            query = form.cleaned_data.get('query')
            if query:
                resultados = Producto.objects.filter(
                    Q(nombre__icontains=query) |
                    Q(descripcion__icontains=query)
                )

        return render(request, 'Lupa/busqueda.html', {'form': form, 'resultados': resultados})