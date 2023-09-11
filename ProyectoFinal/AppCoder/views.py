from django.shortcuts import render

# Create your views here.
def inicio_view(request):
    return render(request, "AppCoder/inicio.html")

def cursos_view(request):
    return render(
        request,
        "AppCoder/cursos.html",
        {
            "nombre": "Curso de Python",
            "camadas": [1000, 1001, 1002, 1003, 1004, 1005]
        }
    )