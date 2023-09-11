from django.contrib import admin
from django.urls import path
from django.http import HttpResponse

def cursos_view(request):
    return HttpResponse("CURSOS")

urlpatterns = [
    path('cursos/', cursos_view),
]