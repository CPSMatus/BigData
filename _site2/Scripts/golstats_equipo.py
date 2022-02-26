"""
Este archivo se utiliza para leer las estadisticas por equipo de Golstats
Author: Susana Matus Ruiz
Las columnas a utilizar seran las siguientes:

    OFENSIVA
    5: pases acertados en cancha propia
    6: pases no acertados en cancha propia
    7: pases acertados en cancha rival
    8: pases no acertados en cancha rival
    14: 1 vs 1 exitoso ofensivo
    15: 1 vs 1 exitoso no ofensivo
    21: goles
    22: tiros a gol
    32: faltas recibidas

    DEFENSIVA
    9: balones recuperados en disputa
    13: rechaces
    16: 1 vs 1 exitoso defensivo
    17: 1 vs 1 exitoso no defensivo
    33: faltas cometidas
    36: goles permitidos
    37: tiros a gol recibidos

"""


import pandas as pd
import openpyxl
import json
#send request GET object to APEX
import requests
import time

class Golstats_equipo():

    # name made in constructor
    def __init__(self, filename):
        self.excel = filename
        self.token = {}
        #Header = 5 because is the row position of the names
        self.h = 5
        self.tu_equipo_pos = 0
        self.rival_pos = 0


    def create_token(self):

        #endpoint request get_url
        test_api_url  = 'https://g6d5f1265b0dcaf-dbapex.adb.us-ashburn-1.oraclecloudapps.com/ords/db_apex/jornada/jornada'
        #access token url
        access_token_url = 'https://g6d5f1265b0dcaf-dbapex.adb.us-ashburn-1.oraclecloudapps.com/ords/db_apex/oauth/token'

        #client (application) credentials - located at apim.byu.edu
        client_id = 'wdA3FiHkziQUmMntrjY-qQ..'
        client_secret = 'ZqBOP8uvW79ZMKarGrFBEg..'

        #authentication type
        token_req_payload = {'grant_type': 'client_credentials'}


        token_response = requests.post(access_token_url,
        data=token_req_payload, verify=False, allow_redirects=False,
        auth=(client_id, client_secret))


        if token_response.status_code !=200:
        	print("Failed to obtain token from the OAuth 2.0 server", file=sys.stderr)
        	sys.exit(1)

            ##
            ## 	obtain a token before calling the API for the first time
            ## 	the token is valid for 15 minutes
            ##

        else:

            print("Successfuly obtained a new token")
            tokens = json.loads(token_response.text)
            token = tokens['access_token']

    def select_headers(self):
        equipo_hash_table = {}
        require_columns = [0]
        df = pd.read_excel(self.excel,header = self.h, usecols = require_columns)
        n_equipos = 0
        isContained = False
        df = df.dropna()


        for index, row in df.iterrows():
            for a in range(1,len(equipo_hash_table)):
                if equipo_hash_table[a] ==  row["NOMBRE"]:
                    isContained = True
            if isContained == True:
                break
            #print(n_players , row["Player"] )
            equipo_hash_table[n_equipos] = row["NOMBRE"]
            n_equipos = n_equipos + 1

        for i in equipo_hash_table:
            print(i, ".- " , equipo_hash_table[i])
        value = int(input())

        return value

    def create_ofensiva(self,h,jornada_id,id_equipo):
        #leer el archivo de Golstats
        ofensive_require_columns = [0,5,6,7,8,14,15,21,22,32]
        ofensiva_df = pd.read_excel(self.excel,header =self.h , usecols = ofensive_require_columns)

        #eliminar a los equipos que no corresponden a Puebla
        df_result = ofensiva_df.iloc[[h]]

        jornada_id_num =jornada_id
        print(df_result)


        data = {
            "pases_acertados_cancha_propia": df_result['PASES ACERTADOS EN CANCHA PROPIA'],
            "pases_no_acertados_cancha_propia":df_result['PASES NO ACERTADOS EN CANCHA PROPIA'],
            "pases_acertados_cancha_rival":df_result['PASES ACERTADOS CANCHA RIVAL'],
            "pases_no_acertados_cancha_rival":df_result['PASES NO ACERTADOS CANCHA RIVAL'],
            "goles":df_result['GOLES'],
            "tiros_a_gol":df_result['TIROS A GOL'],
            "faltas_recibidas":df_result['FALTAS RECIBIDAS'],
            "uno_vs_uno_exitoso_ofensivo":df_result['1 VS 1 EXITOSOS OFENSIVOS'],
            "uno_vs_uno_no_exitoso_ofensivo":df_result['1VS1 NO EXITOSO OFENSIVO'],
            "id_jornada":jornada_id_num,
            "id_equipo":id_equipo
        }
        #print(data)

        url_post_ofensiva_golstats = 'https://g6d5f1265b0dcaf-dbapex.adb.us-ashburn-1.oraclecloudapps.com/ords/db_apex/golstats/ofensiva_golstats'

        response = requests.post(url_post_ofensiva_golstats, params = data)
        print(response.status_code)


    def create_defensiva(self,h,jornada_id,id_equipo):
        defensive_require_columns = [9,13,16,17,33,36,37]
        defensiva_df = pd.read_excel(self.excel,header = self.h, usecols = defensive_require_columns)
        #eliminar a los equipos que no corresponden a Puebla
        df_result = defensiva_df.iloc[[h]]

        jornada_id_num =jornada_id

        print(df_result)

        data = {
            "balones_recuperados_disputa": df_result['BALONES RECUPERADOS EN DISPUTA'],
            "rechaces":df_result['RECHACES'],
            "goles_permitidos":df_result['GOLES RECIBIDOS'],
            "tiros_a_gol_recibidos":df_result['TIRO A GOL RECIBIDOS'],
            "faltas_cometidas":df_result['FALTAS COMETIDAS'],
            "uno_vs_uno_exitoso_defensivo":df_result['1 VS 1 EXITOSOS DEFENSIVOS'],
            "uno_vs_uno_no_exitoso_defensivo":df_result['1VS1 NO EXITOSO DEFENSIVO'],
            "id_jornada":jornada_id_num,
            "id_equipo": id_equipo
        }
        #print(data)

        url_post_defensiva_golstats = 'https://g6d5f1265b0dcaf-dbapex.adb.us-ashburn-1.oraclecloudapps.com/ords/db_apex/golstats/defensiva_golstats'

        response = requests.post(url_post_defensiva_golstats, params = data)
        print(response.status_code)


    def create_general(self,h,jornada_id_num):
        general_require_columns = [34,35]
        ofensiva_df = pd.read_excel(self.excel,header = self.h, usecols = general_require_columns)
        #eliminar a los equipos que no corresponden a Puebla
        df_result = ofensiva_df.iloc[[h]]

        print(df_result)


        data = {
            "tarjetas_rojas": df_result['TARJETAS ROJAS'],
            "tarjetas_amarillas": df_result['TARJETAS AMARILLAS'],
            "id_jornada":jornada_id_num

        }
        #print(data)

        url_post_general_golstats = 'https://g6d5f1265b0dcaf-dbapex.adb.us-ashburn-1.oraclecloudapps.com/ords/db_apex/golstats/general_golstats'

        response = requests.post(url_post_general_golstats, params = data)
        print(response.status_code)
