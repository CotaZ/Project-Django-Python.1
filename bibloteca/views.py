from django.views import View  # Importamos la clase View del módulo django.views
from django.shortcuts import render  # Importamos la función render del módulo django.shortcuts - render se utiliza para renderizar una plantilla de Django con un contexto y devolver una respuesta HTTP al cliente.

class HomeView(View):  # Definimos una subclase llamada HomeView que hereda de View
    def get(self, request, *args, **kwargs):
        # Método get que se ejecuta cuando se realiza una solicitud GET a la vista
        context = {
            # Contexto vacío para almacenar datos a pasar a la plantilla
        }
        return render(request, "index.html", context)
        # Renderizamos la plantilla "index.html" con el contexto proporcionado y devolvemos una respuesta HTTP
