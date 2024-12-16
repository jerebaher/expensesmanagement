from django.shortcuts import render

def home(request):

    context = {
        "whatis": "Es un diccionario de python que se envía dentro de la funcion render para acceder a sus valores desde la plantilla"
    }
    return render(request, "templates/home/index.html", context)
