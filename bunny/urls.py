# bunny/urls.py
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth import views as auth_views

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", include("store.urls")),      # raíz del sitio
    path("usuarios/", include("usuarios.urls")),
    path("carrito/", include("carrito.urls")),
    path("Lupa/", include("Lupa.urls")),
    path('login/', auth_views.LoginView.as_view(template_name='registration/login.html'), name='login'),
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
