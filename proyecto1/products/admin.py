from django.contrib import admin
#**IMPORTANTE | Para registrar un modelo seguir los siguientes pasos:
#1) Agregar el import necesario
from products.models import Products

# Register your models here.
#2) Registrar el modelo.
admin.site.register(Products)

#3) Guardar. Una vez hechos estos pasos el modelo estará visible en el panel de control del proyecto (localhost/8080/admin)