from django.urls import path
from .views import inicio,tienda
from . import views

urlpatterns = [
    path('', views.inicio, name='inicio'),
    path('catalogo/', views.catalogo, name='catalogo'),
    path('',views.tienda, name='tienda')
]
