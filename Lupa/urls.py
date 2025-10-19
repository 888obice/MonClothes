from django.urls import path
from . import views

app_name = 'Lupa'
urlpatterns = [
    path('', views.busqueda, name='busqueda'),
]