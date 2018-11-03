from django.shortcuts import render
from django.http import HttpResponse
import requests

from app2.Requerimientos import Polaridad as pol
from app2.Requerimientos import Historico as his
from app2.Requerimientos import Matoneo as mat

import json
import pymongo


# Index view
def index(request):
    return render(request, 'app2/index.html', None)

def Polaridad(request):
	return pol.hacer_requerimiento(request, dar_base_de_datos())

def Historico(request):
	return his.hacer_requerimiento(request, dar_base_de_datos())

def Matoneo(request):
	return mat.hacer_requerimiento(request, dar_base_de_datos())




def dar_base_de_datos():
    with open('app2/static/app2/jsons/db_configuration.json','r') as f:
        data = json.load(f)

        print("mongodb://" + data['client_location'] + "/")
        client = pymongo.MongoClient("mongodb://" + data['client_location'] + "/")
        mydb = client[data["db_name"]]

        return(mydb)

    raise("Hibo un error conectando a la base de datos")
