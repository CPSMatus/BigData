"""
El siguiente script crea un los jugadores que participan en cada jornada,

incluyendo la informacion contenida en la BD:
-Jornadas :)


informacion de WIMU:
-Jugador :)

informacion de Golstats:
-goles_anotados :36
-minutos_jugados :1
-tarjetas_rojas :92
-tarjetas_amarillas :91
-faltas_cometidas :81
-faltas_recibidas :86

informacion agregada por el usuario:
-calificacion
-entra
-sale
-partidos_jugados : +1

Author: Susana Matus
"""
import pandas as pd
import openpyxl
import json
#send request GET object to APEX
import requests
from datetime import date
from datetime import datetime, timedelta
import numpy as np
import sys
from jornada_dataframe import Jornada

class Jugador_jornada:

    # name made in constructor
    def __init__(self,golstats_loc,wimu_excel):
        self.golstats_excel = golstats_loc
        self.wimu_excel = wimu_excel
        self.token = {}
        #Header = 5 because is the row position of the names
        self.h = 5


    def obtain_token(self):
        if (bool(self.token) == False):
            #   #   Obtener la autenticacio del endpoint    #  #
            #access token url
            access_token_url = 'https://g6d5f1265b0dcaf-dbapex.adb.us-ashburn-1.oraclecloudapps.com/ords/db_apex/oauth/token'

            #client (application) credentials - located at apim.byu.edu
            client_id = 'VYBnKhKCD1mHbYfmDgmIOQ..'
            client_secret = 'u6Wkk7p4r2oj-IRtz84CjQ..'

            #authentication type
            token_req_payload = {'grant_type': 'client_credentials'}


            token_response = requests.post(access_token_url,
            data=token_req_payload, verify=False, allow_redirects=False,
            auth=(client_id, client_secret))


            if token_response.status_code != 200:
            	print("Failed to obtain token from the OAuth 2.0 server", file=sys.stderr)
            	sys.exit(1)

            ##
            ## 	obtain a token before calling the API for the first time
            ## 	the token is valid for 15 minutes
            ##

            print("Successfuly obtained a new token")
            tokens = json.loads(token_response.text)
            token = tokens['access_token']

            ##
            ##   call the API with the token
            ##
            api_call_headers = {'Authorization': 'Bearer ' + token}
            return api_call_headers
        else:
            return self.token

    def get_jornada(self):
        #Obtener el ID de la ultima jornada

        #endpoint request get_url
        ultima_jornada  = 'https://g6d5f1265b0dcaf-dbapex.adb.us-ashburn-1.oraclecloudapps.com/ords/db_apex/jornada/ultima_jornada'

        api_call_response = requests.get(ultima_jornada,verify=False)

        #   #   Obtener el torneo en donde insertae del endpoint    #  #

        if	api_call_response.status_code == 401:
            token = get_new_token()
        else:
            items = api_call_response.json()

        jornada_id_num = (int) (items['items'][0]['jornada_id'])
        print(jornada_id_num)
        return jornada_id_num

    def get_jugadores_jornada(self,id_jornada):
        #Obtener el ID de la ultima jornada
        players_array_id = []
        data = {
        'id_jornada':id_jornada
        }
        #endpoint request get_url
        get_jornada_url  = 'https://g6d5f1265b0dcaf-dbapex.adb.us-ashburn-1.oraclecloudapps.com/ords/db_apex/jornada/jugadores_jornada'

        api_call_response = requests.get(get_jornada_url,params = data,verify=False)

        #   #   Obtener el torneo en donde insertae del endpoint    #  #

        if	api_call_response.status_code == 401:
            token = get_new_token()
        else:
            items = api_call_response.json()

        return items['items']


    def get_wimu_players(self):
        api_call_headers = self.obtain_token()
        players = self.fill_players()
        players_name = []
        #endpoint request get_url
        test_api_url  = 'https://g6d5f1265b0dcaf-dbapex.adb.us-ashburn-1.oraclecloudapps.com/ords/db_apex/torneo/jugador'

        str = ""
        print("\nplayers",players)
        for i in players:
            str = str + i + ","

    #    print(str)
        data_params = {'player_values':str}

        api_call_response = requests.get(test_api_url, headers=api_call_headers, params = data_params,verify=False)

        if	api_call_response.status_code == 401:
        	token = get_new_token()
        else:
            items = api_call_response.json()

        #print("\n",items)
        for i in items['items']:
            nombre = i['nombre'] + ' ' + i['apellido']
            players_name.append(nombre)

        return players_name



    def fill_distance (self,players_array,frames):
        blocks =[]
        column_names = ["0-10", "10-20", "20-30","30-40","40-45","45-50","50-60","60-70","70-80","80-90"]
        df = pd.DataFrame(columns = column_names)
        for i in players_array:
            #Obtener la distance(m)
            distance_array = Jornada.get_distance_for_player(players_array[i],frames)
            df.loc[len(df)] = distance_array
            #create NumPy array for 'players'
            blocks.append(players_array[i])

        #add 'blocks' array as new column in DataFrame
        df['Players'] = blocks

        #display the DataFrame

        return df

    def fill_hse(self,players_array,frames):

        blocks =[]
        column_names = ["0-10", "10-20", "20-30","30-40","40-45","45-50","50-60","60-70","70-80","80-90"]
        df = pd.DataFrame(columns = column_names)
        for i in players_array:
            #Obtener la distance(m)
            distance_array = Jornada.get_high_intensisty_distance_for_player(players_array[i],frames)
            df.loc[len(df)] = distance_array
            #create NumPy array for 'players'
            blocks.append(players_array[i])

        #add 'blocks' array as new column in DataFrame
        df['Players'] = blocks

        #display the DataFrame

        return df

    def fill_sprints(self,players_array,frames):
        blocks =[]
        column_names = ["0-10", "10-20", "20-30","30-40","40-45","45-50","50-60","60-70","70-80","80-90"]
        df = pd.DataFrame(columns = column_names)
        for i in players_array:
            #Obtener la distance(m)
            sprint_array = Jornada.get_sprints_for_player(players_array[i],frames)
            df.loc[len(df)] = sprint_array
            #create NumPy array for 'players'
            blocks.append(players_array[i])


        #add 'blocks' array as new column in DataFrame
        df['Players'] = blocks

        #display the DataFrame

        return df



    def post_wimu_values(self,players_array,frames,items):

        df_distance = self.fill_distance(players_array,frames)
        print('\nDistance')
        print(df_distance)

        counter = 1
        for index, row in df_distance.iterrows():
            for i in items:
                if i['wimu_alias'] == row[10]:
                    id_jugador_jornada = i['jugador_jornada_id']
                    #print(i['wimu_alias'] , id_jugador_jornada)
                    break
            data = {
                "i_0_10": row[0],
                "i_10_20": row[1],
                "i_20_30": row[2],

                "i_30_40": row[3],
                "i_40_45": row[4],
                "i_45_50": row[5],

                "i_50_60": row[6],
                "i_60_70": row[7],
                "i_70_80": row[8],

                "i_80_90": row[9],
                "id_jugador_jornada":id_jugador_jornada

            }
            url_golstats_jugador_posicion = "https://g6d5f1265b0dcaf-dbapex.adb.us-ashburn-1.oraclecloudapps.com/ords/db_apex/jornada/wimu_distance_jornada"

            api_call_sesion_response = requests.post(url_golstats_jugador_posicion, params = data,verify=False)
            #api_call_sesion_response = requests.post(url_jugador_sesion, headers=api_call_headers, params = data,verify=False)
            print(counter, ".- ", row[10], api_call_sesion_response.status_code)
            counter = counter + 1


        df_hse = self.fill_hse(players_array,frames)
        print('\nHSE')
        print(df_hse)

        counter = 1
        for index, row in df_hse.iterrows():
            for i in items:
                if i['wimu_alias'] == row[10]:
                    id_jugador_jornada = i['jugador_jornada_id']
                    #print(i['wimu_alias'] , id_jugador_jornada)
                    break
            data = {
                "i_0_10": row[0],
                "i_10_20": row[1],
                "i_20_30": row[2],

                "i_30_40": row[3],
                "i_40_45": row[4],
                "i_45_50": row[5],

                "i_50_60": row[6],
                "i_60_70": row[7],
                "i_70_80": row[8],

                "i_80_90": row[9],
                "id_jugador_jornada":id_jugador_jornada

            }
            url_golstats_jugador_posicion = "https://g6d5f1265b0dcaf-dbapex.adb.us-ashburn-1.oraclecloudapps.com/ords/db_apex/jornada/wimu_hse_jornada"

            api_call_sesion_response = requests.post(url_golstats_jugador_posicion, params = data,verify=False)
            #api_call_sesion_response = requests.post(url_jugador_sesion, headers=api_call_headers, params = data,verify=False)
            print(counter, ".- ", row[10], api_call_sesion_response.status_code)
            counter = counter + 1



        df_sprints = self.fill_sprints(players_array,frames)
        print('\nSprints')
        print(df_sprints)

        counter = 1
        for index, row in df_sprints.iterrows():
            for i in items:
                if i['wimu_alias'] == row[10]:
                    id_jugador_jornada = i['jugador_jornada_id']
                    #print(i['wimu_alias'] , id_jugador_jornada)
                    break
            data = {
                "i_0_10": row[0],
                "i_10_20": row[1],
                "i_20_30": row[2],

                "i_30_40": row[3],
                "i_40_45": row[4],
                "i_45_50": row[5],

                "i_50_60": row[6],
                "i_60_70": row[7],
                "i_70_80": row[8],

                "i_80_90": row[9],
                "id_jugador_jornada":id_jugador_jornada

            }
            url_golstats_jugador_posicion = "https://g6d5f1265b0dcaf-dbapex.adb.us-ashburn-1.oraclecloudapps.com/ords/db_apex/jornada/wimu_sprints_jornada"

            api_call_sesion_response = requests.post(url_golstats_jugador_posicion, params = data,verify=False)
            #api_call_sesion_response = requests.post(url_jugador_sesion, headers=api_call_headers, params = data,verify=False)
            print(counter, ".- ", row[10], api_call_sesion_response.status_code)
            counter = counter + 1
