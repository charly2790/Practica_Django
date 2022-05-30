from django.db import models

# Create your models here.
class Products(models.Model):
    name = models.CharField(max_length=40)
    price = models.FloatField()
    #**IMPORTANTE | A cont. definimos un campo que tiene un max. de 200 caract. PUEDE venir en blanco y PUEDE venir nulo.
    description = models.CharField(max_length=200,blank=True,null=True)
    SKU = models.CharField(max_length=30,unique=True)
    #**IMPORTANTE | A cont. definimos un campo booleano que por default viene en True
    activate = models.BooleanField(default=True)

    #**IMPORTANTE | Es necesario correr el comando: 
    #******************************************python manage.py makemigrations******************************************
    #**Makemigrations -> Mediante una migración Django traduce el modelo a SQL. Se observa que la aplicación
    #actual (products) tiene un subdirectorio llamado 'migrations' el cual solo contiene un achivo '__init__'
    #al ejecutar el comando debería aparecer 'XXXX_initial.py' que contiene instrucciones para generar las tablas
    #de base de datos sobre el archivo db.sqliteX. 
    #Finalmente es necesario ejecutar el comando 
    #**********************************************python manage.py migrate*********************************************
    #De esta manera se generan al fin la/las tabla/s relacionadas al modelo.
    
    #Una vez realizado lo anterior, el modelo aún no esta listo para visualizarse en el panel de control del proyecto django (localhost:8080/admin)
    #Para poder visualizarlo ahi, hay que registrar el modelo ¿Donde? en el archivo admin.py
