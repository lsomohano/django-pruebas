from ast import Return
from curses.ascii import HT
from datetime import datetime
from pipes import Template
from django.http import HttpResponse
from django.template import Template,Context
from django.template.loader import get_template
from django.shortcuts import render
import os
import json
import io

class persona(object):
    def __init__(self, nombre, apellido) -> None:
        self.nombre=nombre
        self.apellido=apellido

def saludo(request):

    p1 = persona("Leonel","Somohano Carmona")
    fecha_actual=datetime.now()

    #doc_externo = open("plantillas/miplantilla.html","r")
    #plantilla = Template(doc_externo.read())
    #doc_externo.close()
    #doc_externo = get_template('miplantilla.html')

    #contexto = Context({"nombre_persona":p1.nombre,"apellido_persona":p1.apellido,"fecha_actual":fecha_actual,"temas":["Plantillas","Modelos","Formularios","Vistas","Despliegues"]})

    #documento=doc_externo.render(contexto)

    #return HttpResponse(documento)
    return render(request, "miplantilla2.html",{"nombre_persona":p1.nombre,"apellido_persona":p1.apellido,"fecha_actual":fecha_actual,"temas":["Plantillas","Modelos","Formularios","Vistas","Despliegues"]})

def despedida(request):
    return HttpResponse("Adios!, esta es una depedida")

def dame_fecha(request):
    fecha_actual=datetime.now()
    domcumento = "La fecha actual es; %s" % fecha_actual
    return HttpResponse(domcumento)

def calcula_edad(request, edad, agno):
    #edadActual = 37
    periodo = agno - 2022
    edadFutura = edad + periodo
    documento = "<html><body><h2> En el año %s tendras %s años" %(agno,edadFutura)
    return HttpResponse(documento)

#Lee un los archivos JSON de la carpeta Inspections
def lee_archivos(request, economico):
    
    path = '/code/prueba/static/reconpro/20211224/Inspections/'
    dirs = os.listdir(path)
    path_img = '/code/prueba/static/reconpro/20211224/'
    data = {}

    for file in dirs:
        doc_externo = io.open(path + file, 'r', encoding='latin-1')
        doc_read = json.load(doc_externo)
        doc_externo.close()

        if doc_read["StockNo"] == economico or doc_read["RONo"] == economico:
            data = doc_read

    return render(request, "reconpro.html",{"data":data, "path_img":path_img})
