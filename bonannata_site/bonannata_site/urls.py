from django.contrib import admin
from django.urls import path, include
from django_distill import distill_path
from landing import views

# Vistas que se renderizaran como HTML estático
def get_index():
    return {}

urlpatterns = [
    path('admin/', admin.site.urls),
    distill_path('', views.index, name='index', distill_func=get_index),
]

# Para desarrollo normal, agregar incluir landing.urls
if False:  # Cambia a True si quieres usar development server normal
    urlpatterns += [
        path('', include('landing.urls')),
    ]
