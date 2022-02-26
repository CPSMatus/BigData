"""
Este script se utiliza para leer los archivos de WIMU y seleccionar las estadisticas a utilizar para
posteriormente ser posteada a la BD.

Author: Susana Matus Ruiz
Las columnas a utilizar seran las siguientes:

    SHEETS
    [0,1,3,8]

    0: Distance
    1: Acceleration
    3: HSE
    8: Load



"""

import pandas as pd
import openpyxl
import json
#send request GET object to APEX
import requests
from datetime import date
from datetime import datetime, timedelta
import numpy as np



class Pf_diario:

    # name made in constructor
    def __init__(self, filename,loc):
        self.excel = loc + filename
        self.token = {}

    def get_last_session_info(self,api_call_headers):

    #    #    #    #     OBTENER EL ID DE LA SESION DE ENTRENAMIENTO     #    #   #  #
        url_ultima_sesion_entrenamiento = "https://g6d5f1265b0dcaf-dbapex.adb.us-ashburn-1.oraclecloudapps.com/ords/db_apex/sesion/last_sesion"

        api_call_sesion_response = requests.get(url_ultima_sesion_entrenamiento, headers=api_call_headers,verify=False)


        if	api_call_sesion_response.status_code == 401:
        	token = get_new_token()
        else:

            id_sesion_json = api_call_sesion_response.json()


        sesion_id_num = (int) (id_sesion_json['items'][0]['sesion_entrenamiento_id'])
        print(sesion_id_num)

        return sesion_id_num

    def crear_jugador_sesion(self,api_call_headers):
        players = self.fill_players()

        #endpoint request get_url
        test_api_url  = 'https://g6d5f1265b0dcaf-dbapex.adb.us-ashburn-1.oraclecloudapps.com/ords/db_apex/torneo/jugador'

        str = ""

        for i in players:
            str = str + i + ","

    #    print(str)
        data_params = {'player_values':str}

        api_call_response = requests.get(test_api_url, headers=api_call_headers, params = data_params,verify=False)


        if	api_call_response.status_code == 401:
        	token = get_new_token()
        else:
            items = api_call_response.json()


        sesion_id_num = self.get_last_session_info(api_call_headers)
        df_final = self.create_dill_df()
        #df_final['ID_SESION_ENTRENAMIENTO'] = sesion_id_num

        print("\n",df_final, sesion_id_num)

        #obtener el URL para poster la duracion del drill en la BD
        url_jugador_sesion = "https://g6d5f1265b0dcaf-dbapex.adb.us-ashburn-1.oraclecloudapps.com/ords/db_apex/sesion/jugador_sesion"

        counter= 1
        #for index, row in drill_duration_df.iterrows():
        for index, row in df_final.iterrows():
            data = {
                "drill_duration": row[1],
                "jugador": row[0],
                "id_sesion_entrenamiento":sesion_id_num ,
            }

            api_call_sesion_response = requests.post(url_jugador_sesion, headers=api_call_headers, params = data,verify=False)
            print(row[0])
            print(counter, ".- ", api_call_sesion_response.status_code)
            counter = counter + 1

    def  crear_sesion_entrenamiento(self,api_call_headers,data_params,n_microciclo,sesion,lugar_entrenamiento,fecha):

        #    #    #    #     GET THE ID DEL TORNEO     #    #   #  #


        #endpoint request get_url
        test_api_url  = 'https://g6d5f1265b0dcaf-dbapex.adb.us-ashburn-1.oraclecloudapps.com/ords/db_apex/torneo/torneo'

        api_call_response = requests.get(test_api_url, headers=api_call_headers, params = data_params,verify=False)

        #   #   Obtener el torneo en donde insertae del endpoint    #  #

        if	api_call_response.status_code == 401:
        	token = get_new_token()
        else:
            items = api_call_response.json()

        torneo_id_num = (int) (items['items'][0]['torneo_id'])


        #    #    #    #     POST SESION DE ENTRENAMIENTO THE ID DEL TORNEO     #    #   #  #
        # 0 : ALPHA
        # 2 : ESTADIO CUAUTEMOC
        # 3 : OTRO
        print(fecha)
        data = {
            "fecha": fecha,
            "n_microciclo": n_microciclo,
            "sesion": sesion,
            "id_torneo": torneo_id_num,
            "id_lugar": lugar_entrenamiento,
        }

        url = "https://g6d5f1265b0dcaf-dbapex.adb.us-ashburn-1.oraclecloudapps.com/ords/db_apex/torneo/sesion_entrenamiento"


        response = requests.post(url,headers=api_call_headers, params = data,verify=False)
        print(response.status_code)

    def get_last_session_wimu_info(self,api_call_headers):

    #    #    #    #     OBTENER EL ID DE LA SESION DE ENTRENAMIENTO     #    #   #  #
        url_ultima_sesion_entrenamiento = "https://g6d5f1265b0dcaf-dbapex.adb.us-ashburn-1.oraclecloudapps.com/ords/db_apex/sesion/last_sesion_wimu_data"

        api_call_sesion_response = requests.get(url_ultima_sesion_entrenamiento, headers=api_call_headers,verify=False)


        if	api_call_sesion_response.status_code == 401:
        	token = get_new_token()
        else:
            data = api_call_sesion_response.json()

        return data

    def fill_players(self):

        #Se llena un hashtable con los jugadores que participaron en la sesion
        players = []
        require_cols_sheet_0 = [0,2]

        isContained = False
        dataframe = pd.read_excel(self.excel, usecols = require_cols_sheet_0)
        #Delete first and last row because they contain NaN values
        dataframe = dataframe.dropna()
        #cuantos jugaron todo el partido
        for index, row in dataframe.iterrows():
            for a in range(0,len(players)):
                if players[a] ==  row["Player"]:
                    isContained = True
            if isContained == True:
                break

            players.append(row["Player"])

        print(players)

        return players



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


    def create_m_min_df(self):

        counter = 0
        require_cols_sheet_0_duration = [0,2,4]
        #Obtener la duracion del drills
        m_min_df = pd.read_excel(self.excel, usecols = require_cols_sheet_0_duration)
        row_m_min = []

    #       Change time to minutes

        #cut the DF
        for index, row in m_min_df.iterrows():

            if (pd.isna(row["Player"]) and counter > 2):
                lap0_to = counter
                break
            counter = counter + 1

        m_min_df = m_min_df.iloc[2:lap0_to,:]


        for index, row in m_min_df.iterrows():
            if(pd.isna(row[1])):
                continue

            datetime_object = row[1].split(':')
            #Change hour format to minutes
            minutestime_int = ((int)(datetime_object[0])) * 60 + (int) (datetime_object[1])
            #calcular los metros / min
            m_min = round ((row[2] / minutestime_int),2)
            #cambiar el valor de la duracion del drill

            row_m_min.append(m_min)


        m_min_df['M_MIN'] = row_m_min


        return m_min_df


    def create_dill_df(self):
        require_cols_sheet_0_duration = [0,2]
        #Obtener la duracion del drills
        drill_duration_df = pd.read_excel(self.excel, usecols = require_cols_sheet_0_duration)

        counter = 0
        #cut the DF
        for index, row in drill_duration_df.iterrows():

            if (pd.isna(row["Player"]) and counter > 2):
                lap0_to = counter
                break
            counter = counter + 1
        df_final = drill_duration_df.iloc[2:lap0_to,:]



    #       Change time to minutes
        for index, row in df_final.iterrows():
            if(pd.isna(row[1])):
                continue
            time = str(row[1])
            datetime_object = time.split(':')

            #Change hour format to minutes
            minutestime_int = ((int)(datetime_object[0])) * 60 + (int) (datetime_object[1])
            seconds = datetime_object[2].split('.')

            minutes_object = '{minutes}:{seconds}'.format(minutes=minutestime_int, seconds=(seconds[0]))
            row[1] = minutes_object
            #s = pd.Series(row[1])
            #s = pd.to_timedelta(row[1])


        #print(df_final)
        return df_final

    def create_df(self):

        distance_sheet = 0
        acceleration_sheet = 1
        hse_sheet = 3
        load_sheet = 8

        counter = 0

        require_cols_sheet_0 = [0,4,5]
        require_cols_sheet_0_duration = [0,2]
        require_cols_sheet_1 = [16,17,18,19]
        require_cols_sheet_3 = [9]
        require_cols_sheet_8 = [3,14]
        row = []

        #adding one row to put them in the same position
        row.insert(0,{'HSR Abs (m)':0})
        #reading hse excel
        r =  pd.read_excel(self.excel, sheet_name = hse_sheet, usecols = require_cols_sheet_3)
        #inserting one empty row
        hse_df = pd.concat([pd.DataFrame(row), r], ignore_index=True)
        #print(hse_df)

        #reading sheet 0 excel
        distance_df = pd.read_excel(self.excel, usecols = require_cols_sheet_0)
        #print(distance_df.head(50))

        #reading sheet 1 excel
        acceleration_df = pd.read_excel(self.excel, sheet_name = acceleration_sheet, usecols = require_cols_sheet_1)

        #reading sheet 8 excel
        load_df = pd.read_excel(self.excel, sheet_name = load_sheet, usecols = require_cols_sheet_8)
        #print(load_df)


        #appending the three frames together
        df_pre_result = [distance_df,hse_df,acceleration_df,load_df]
        df_result = pd.concat(df_pre_result, axis = 1, sort = False)
        #print(df_result.head(50))

        for index, row in df_result.iterrows():

            if (pd.isna(row["Player"]) and counter > 2):
                lap0_to = counter
                break
            counter = counter + 1

        df_result = df_result.iloc[2:lap0_to]

        return df_result


    def crear_wimu_sesion_data(self,api_call_headers):


        m_min_df = self.create_m_min_df()

        wimu_df = self.create_df()

        df_pre_result = [wimu_df,m_min_df['M_MIN']]
        df_result = pd.concat(df_pre_result, axis = 1, sort = False)


        #obtener el URL para poster los valores obtenidos
        url_jugador_sesion = "https://g6d5f1265b0dcaf-dbapex.adb.us-ashburn-1.oraclecloudapps.com/ords/db_apex/sesion/wimu_sesion_data"
        sesion_id_num = self.get_last_session_info(api_call_headers)
        print(df_result)

        counter= 1

        #Enviar a cada jugador a la base de datos
        for index, row in df_result.iterrows():

            data = {
                "jugador": row[0],
                "id_sesion_entrenamiento": sesion_id_num,
                "total_distance": row[1],
                "explosive_distance":row[2],
                "hsr_abs":row[3],
                "high_acc_count":row[4],
                "high_dec_count":row[5],
                "high_acc_m":row[6],
                "high_dec_m":row[7],
                "player_load":row[8],
                "hmld":row[9],
                "m_min":row[10]
            }

            api_call_sesion_response = requests.post(url_jugador_sesion, headers=api_call_headers, params = data,verify=False)
            print(counter, ".- ", api_call_sesion_response.status_code)
            counter = counter + 1

        return df_result

    def crear_wimu_sesion_data_xls(self,api_call_headers):

        distance_sheet = 0
        acceleration_sheet = 1

        load_sheet = 9
        counter = 0

        require_cols_sheet_0 = [0,3,4,5,13]
        #require_cols_sheet_0_duration = [0,2]
        require_cols_sheet_1 = [11,12,13,14]
        require_cols_sheet_9 = [2,13]
        row = []

        #reading sheet 0 excel
        distance_df = pd.read_excel(self.excel, usecols = require_cols_sheet_0)
        print(distance_df)

        #reading sheet 1 excel
        acceleration_df = pd.read_excel(self.excel, sheet_name = acceleration_sheet, usecols = require_cols_sheet_1)
        print(acceleration_df)

        #reading sheet 9 excel
        load_df = pd.read_excel(self.excel, sheet_name = load_sheet, usecols = require_cols_sheet_9)
        print(load_df)


        #appending the three frames together
        df_pre_result = [distance_df,acceleration_df,load_df]
        df_result = pd.concat(df_pre_result, axis = 1, sort = False)
        #print(df_result.head(50))

        for index, row in df_result.iterrows():

            if (pd.isna(row["Player"]) and counter > 2):
                lap0_to = counter
                break
            counter = counter + 1

        df_result = df_result.iloc[2:lap0_to]


        #get the number of columns
        n = df_result.shape[1]
        val = []
        for col in df_result:
             # Select column contents by column name using [] operator
            columnSeriesObj = df_result[col]
            if (col == "Player"):
                continue

            for i in columnSeriesObj.values:
                val.append(round(i,2))
            df_result[col] = df_result[col].replace(columnSeriesObj.values,val)
            val.clear()

            #print('Colunm Name : ', col)
            #print('Column Contents : ', columnSeriesObj.values)


        #print("\n, the number of columns is :", n)
        print(df_result)


        # URL para poster los valores obtenidos
        url_jugador_sesion = "https://g6d5f1265b0dcaf-dbapex.adb.us-ashburn-1.oraclecloudapps.com/ords/db_apex/sesion/wimu_sesion_data"



        #Enviar a cada jugador a la base de datos
        for index, row in df_result.iterrows():
            data = {
                "jugador": row[0],
                "total_distance": row[1],
                "explosive_distance":row[3],
                "hsr_abs":row[4],
                "high_acc_count":row[5],
                "high_dec_count":row[6],
                "high_acc_m":row[7],
                "high_dec_m":row[8],
                "player_load":row[9],
                "hmld":row[10],
                "m_min":row[2]
            }
            api_call_sesion_response = requests.post(url_jugador_sesion, headers=api_call_headers, params = data,verify=False)
            print(api_call_sesion_response.status_code)

        return df_result
