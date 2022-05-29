from contextvars import Context
from django.http import HttpResponse
from django.template import Template, Context
from datetime import datetime



def saludo(request,nombre):
    return HttpResponse(f'<h1 style="color: red;">River Campeón Libertadores 2022 {nombre}</h1>')

def fecha_actual(request):
    fecha= datetime.now()
    mensaje = f'Hoy es {fecha}'
    return HttpResponse(mensaje)

def probando_template(request):
    mi_html = open(r"C:\Users\charl\Documents\Cursos\Python - Coderhouse\Django_1\proyecto1\templates\template1.html")

    plantilla = Template(mi_html.read())

    mi_html.close()

    mi_contexto = Context()

    documento = plantilla.render(mi_contexto)

    return HttpResponse(documento)