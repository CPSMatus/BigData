
import pandas as pd
import openpyxl
import json
#send request GET object to APEX
import requests
from datetime import date
from datetime import datetime, timedelta
import numpy as np



class Resumen_torneo:

    # name made in constructor
    def __init__(self):
        self.id_torneo = 4
        #self.token = {}


    def get_jornadas(self):

    #    #    #    #     OBTENER EL ID DE LA SESION DE ENTRENAMIENTO     #    #   #  #
        url_jornadas = "https://g6d5f1265b0dcaf-dbapex.adb.us-ashburn-1.oraclecloudapps.com/ords/db_apex/jornada/jornadas"

        data = {
        'id_torneo': 1
        }

        api_call_sesion_response = requests.get(url_jornadas, params = data,verify=False)

        data = api_call_sesion_response.json()

        return data

    def get_jugadores(self):

    #    #    #    #     OBTENER TODOS LOS JUGADORES ACTIVOS    #    #   #  #
        jugadores = "https://g6d5f1265b0dcaf-dbapex.adb.us-ashburn-1.oraclecloudapps.com/ords/db_apex/general/jugadores"


        api_call_sesion_response = requests.get(jugadores,verify=False)

        data = api_call_sesion_response.json()

        return data


    def get_jugadores_jornada(self):

        data = {
        'id_torneo': 1
        }
    #    #    #    #     OBTENER TODOS LOS JUGADORES ACTIVOS    #    #   #  #
        jugadores_jornadas = "https://g6d5f1265b0dcaf-dbapex.adb.us-ashburn-1.oraclecloudapps.com/ords/db_apex/jornada/jugador_jornadas"

        api_call_sesion_response = requests.get(jugadores_jornadas,params = data,verify=False)

        data = api_call_sesion_response.json()

        return data
