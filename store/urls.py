from django.urls import path
from .views import inicio
from . import views

urlpatterns = [
    path('', inicio, name='inicio'),
     path('catalogo/', views.catalogo, name='catalogo'),
]
