from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import authentication, permissions
from django.contrib.auth.forms import AuthenticationForm
from django.http import HttpResponse
from django.template import Template, Context
from django.template import RequestContext
from django.shortcuts import render,redirect

from datetime import datetime
import sys
import json
import requests
import numpy as np
from django import forms


sys.path.insert(0,'/Users/smatus/Documents/Python by example/project 1/_site2/Scripts')

from jornada_dataframe import Jornada
from sum_player_jornada import Mean_player_jornada

from mean_team_minuto import Mean_team_minuto
from mean_team_jornada import Mean_team_jornada




def index_areas (request): #primera vista
    return render(request,'index_areas.html') #HttpResponse(documento)

def resumen_partido(request):
    return render(request,'resumen_partido_table.html')



class chartData(APIView):
    authentication_classes = []
    permission_classes = []

    def get(self, request, format=None):
        selected_jornada = "J15 AP 2021.xlsx"
        #crear eje x
        minutes_interval = Jornada.send_minutes_interval()
        #seleccionar al jugador a evaluar
        selected_player = Jornada.select_player(selected_jornada)
        #Extraer las columnas del excel para analizar solo el dataframe
        result = Jornada.create_df(selected_jornada)
        #Obtener los lapsos a examinar, eliminar drills y primer tiempo
        frames = Jornada.create_df_parameters(result)


        #Obtener la distance(m)
        distance_array = Jornada.get_distance_for_player(selected_player,frames)

        labels = minutes_interval
        default_items = distance_array
        data = {
            "labels":labels,
            "default":default_items,
        }
        return Response(data)
