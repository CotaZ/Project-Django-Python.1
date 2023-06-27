from django.contrib import admin  # Importamos el módulo admin de Django para la administración
from django.urls import path, include  # Importamos la función path para definir las rutas URL
from .views import HomeView  # Importamos la vista HomeView desde el archivo views.py

urlpatterns = [
    path('admin/', admin.site.urls),  # URL para acceder al panel de administración de Django
    path('', HomeView.as_view(), name="home"),  # URL raíz que utiliza la vista HomeView y se le asigna el nombre "home"
    path('blog/', include('blog.urls', namespace='blog')) # URL raíz que utiliza la vista HomeView y se le asigna el nombre "blog"
]
