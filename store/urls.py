# store/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="inicio"),        # Home: elige index como página principal
    path("catalogo/", views.catalogo, name="catalogo"),
    path("tienda/", views.tienda, name="tienda"),  # o elimina si duplicado
    path('buscar/', views.buscar_productos, name='buscar_productos'),
]
