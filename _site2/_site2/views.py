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
from pf_diario import Pf_diario
from mean_team_minuto import Mean_team_minuto
from mean_team_jornada import Mean_team_jornada


c = Pf_diario('','')




def index_areas (request): #primera vista
    return render(request,'index_areas.html') #HttpResponse(documento)

def resumen_partido(request):
    return render(request,'resumen_partido_table.html')


def table_jugadores(request):

    data = endpoint_torneo.get_jugadores()


    context={'jugadores' : data['items']}
    #print(context)
    return render(request,'table_jugadores.html',context)


def resumen_entrenamiento_filtros(request):
    return render(request,'resumen_entrenamiento_table2.html')


def resumen_entrenamiento(request):

    #si el metodo es post, esta llamada proviene del boton de filtrado
    if request.method =='POST':
        from_calendar = datetime.now()
        to_calendar = datetime.now()
        player = request.POST['players_select']
        #Obtener a los jugadores de la ultima sesion ! ! ! ! ! !! !! ! ! ! !! ! !! !
        from_calendar = request.POST['calendar_from']
        to_calendar = request.POST['calendar_to']
        posicion = request.POST['posicion_select']
        api_call_headers = c.obtain_token()

        # jugador - posicion
        if( (player != 0) and (posicion != 0)):
            print('calendar - jugador - posicion')
        # jugador -
        if( (player != 0) and (posicion == 0)):
            print('calendar - jugador - posicion')

        #        - posicion
        if( (player == 0) and (posicion != 0)):
            print('calendar - jugador - posicion')

        #        - posicion
        if( (player == 0) and (posicion != 0)):
            print('calendar - jugador - posicion')




        print(player)
        print(from_calendar)
        print(to_calendar)
        print(posicion)

#Si el metodo es get, se da lectura, es decir se requieren los datos de la ultima sesion
    #if request.method =='GET':
    api_call_headers = c.obtain_token()
    table_list = c.get_last_session_wimu_info(api_call_headers)
    context={'table_list' : table_list['items']}

    return render(request,'resumen_entrenamiento_table2.html',context)


def dashboard_jugador(request):
    selected_player= "DIEGO DE BUEN"
    jornadas_excel_array = np.array(["J01 AP 2021.xlsx",
                                "J02 AP 2021.xlsx",
                                "J03 AP 2021.xlsx",
                                "J04 AP 2021.xlsx",
                                "J05 AP 2021.xlsx",
                                "J06 AP 2021.xlsx",
                                "J07 AP 2021.xlsx",
                                "J08 AP 2021.xlsx",
                                "J09 AP 2021.xlsx",
                                "J10 AP 2021.xlsx",
                                "J11 AP 2021.xlsx",
                                "J12 AP 2021.xlsx",
                                "J13 AP 2021.xlsx",
                                "J14 AP 2021.xlsx",
                                "J15 AP 2021.xlsx",
                                "J16 AP 2021.xlsx",
                                "J17 AP 2021.xlsx"
                                ])

    #Analisis jugador x Jornada
    distance_array_mean = Mean_player_jornada.select_distance_values(jornadas_excel_array,selected_player)

    high_intensity_distance_array_mean = Mean_player_jornada.select_high_intensity_distance_values(jornadas_excel_array, selected_player)

    sprint_abs_cnt_array_mean = Mean_player_jornada.select_sprint_abs_cnt_values(jornadas_excel_array, selected_player)

    #enviamos las jornadas al eje x
    jornadas_eje_x = Mean_player_jornada.set_x_range()

    labels = jornadas_eje_x.tolist()

    print(labels)
    print(distance_array_mean)

    data = {
        "labels": labels,
        "labels2": labels,
        "labels3": labels,
        "distance_array_mean": distance_array_mean,
        "high_intensity_distance_array_mean": high_intensity_distance_array_mean,
        "sprint_abs_cnt_array_mean": sprint_abs_cnt_array_mean,

    }


    return render(request,'dashboard_jugador.html',context = data)

def analisis_jugador_jornada(request):

    selected_jornada = "J16 AP 2021.xlsx"
    #crear eje x
    minutes_interval = Jornada.send_minutes_interval()
    #seleccionar al jugador a evaluar
    selected_player = request.GET["player_name"]
    print(selected_player)
    #Extraer las columnas del excel para analizar solo el dataframe
    result = Jornada.create_df(selected_jornada)
    #Obtener los lapsos a examinar, eliminar drills y primer tiempo
    frames = Jornada.create_df_parameters(result)
    #Obtener la distance(m)
    distance_array = Jornada.get_distance_for_player(selected_player,frames)

    #Obtener la distance(m) en alta intensidad
    high_intensity_distance_array = Jornada.get_high_intensisty_distance_for_player(selected_player,frames)
    #Obtener los sprints
    sprint_abs_cnt_array = Jornada.get_sprints_for_player(selected_player,frames)
    #Rellenar el arreglo con los jugadores que participaron en la Jornada a analizar
    players_hash_table = Jornada.fill_players(selected_jornada)
    distance_array_mean_team = Mean_team_minuto.select_distance_team_values(players_hash_table,frames)

    labels = minutes_interval.tolist()



    print(labels)
    print(distance_array)

    data = {
        "labels": labels,
        "labels2": labels,
        "labels3": labels,
        "labels4": labels,
        "distance": distance_array,
        "high_intensity_distance_array": high_intensity_distance_array,
        "sprint_abs_cnt_array": sprint_abs_cnt_array,
        "distance_array_mean_team":distance_array_mean_team

    }

    return render(request,'resumen_jugador_xpartido.html',context = data)

def analisis_torneo(request):


    jornadas_excel_array = np.array(["J01 AP 2021.xlsx",
                                "J02 AP 2021.xlsx",
                                "J03 AP 2021.xlsx",
                                "J04 AP 2021.xlsx",
                                "J05 AP 2021.xlsx",
                                "J06 AP 2021.xlsx",
                                "J07 AP 2021.xlsx",
                                "J08 AP 2021.xlsx",
                                "J09 AP 2021.xlsx",
                                "J10 AP 2021.xlsx",
                                "J11 AP 2021.xlsx",
                                "J12 AP 2021.xlsx",
                                "J13 AP 2021.xlsx",
                                "J14 AP 2021.xlsx",
                                "J15 AP 2021.xlsx",
                                "J16 AP 2021.xlsx"
                                ])


    #enviamos las jornadas al eje x
    x_mean_interval = Mean_team_jornada.set_x_range()

    ##Arrays for team x Jornada
    distance_array_mean_jornada = Mean_team_jornada.select_distance_values(jornadas_excel_array)

    hi_distance_array_mean_jornada = Mean_team_jornada.select_high_intensity_distance_values(jornadas_excel_array)

    sprint_abs_cnt_array_mean_jornada = Mean_team_jornada.select_sprint_abs_cnt_values(jornadas_excel_array)
    x_mean_interval_list = x_mean_interval.tolist()
    data = {
        "distance_array_mean_jornada": distance_array_mean_jornada,
        "hi_distance_array_mean_jornada": hi_distance_array_mean_jornada,
        "sprint_abs_cnt_array_mean_jornada": sprint_abs_cnt_array_mean_jornada,

        "x_mean_interval": x_mean_interval_list


    }

    return render(request,'analisis_torneo.html',context = data)



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
