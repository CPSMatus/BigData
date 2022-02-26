import json
import requests
import pandas as pd
import json

class Jugador_x_partido_handler():

    def get_jugador_x_partido(self,id_jugador_jornada):
        #Obtener la informacion para este partido



        test_api_url  = 'https://g6d5f1265b0dcaf-dbapex.adb.us-ashburn-1.oraclecloudapps.com/ords/db_apex/resumen/jugador_x_jornada'
        data = {
            'id_jugador_jornada' :id_jugador_jornada
        }

        api_call_response = requests.get(test_api_url, params = data)

        #   #   Obtener la JORNADA  en donde se insertara el endpoint    #  #

        if	api_call_response.status_code == 401:
        	token = get_new_token()
        else:
            items = api_call_response.json()

        return items['items'][0]
