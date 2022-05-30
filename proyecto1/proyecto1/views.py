from contextvars import Context
from django.http import HttpResponse
from django.template import Template, Context
from datetime import datetime

#**IMPORTANTE | Necesario para redireccionar templates junto con un cambio adicional en el archivo settings
from django.shortcuts import render



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

#Paso 1) Agregar la view
def probando_render_template(request):

    anios_campeon = [1986,1996,2015,2018]
    #con datetime.now() obtengo la fecha actual    
    context = {'nombre':'Carlos','apellido':'Barrionuevo','fecha':datetime.now(),'anios_campeon':anios_campeon}

    return render(request,'template_2.html',context=context)