"""
URL configuration for tech project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.contrib import admin
from django.urls import path, include
from django.contrib.auth import views as auth_views  # 👈  importa las vistas auth
from inventario_tech.views import bienvenida  # (tu vista de portada)
from django.contrib.auth.views import LogoutView

urlpatterns = [
    path("", bienvenida, name="home"),
    # Login / logout  —— usa TU plantilla
    path(
        "accounts/login/",
        auth_views.LoginView.as_view(template_name="inventario_tech/login.html"),
        name="login",
    ),
    path(
        "accounts/logout/",
        auth_views.LogoutView.as_view(next_page="home"),  # 👈 redirige a la portada
        name="logout",
    ),
    # Resto de rutas
    path("admin/", admin.site.urls),
    path("inventario/", include(("inventario_tech.urls", "inventario_tech"))),
]
