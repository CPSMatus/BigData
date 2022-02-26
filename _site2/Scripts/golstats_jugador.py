


import pandas as pd
import openpyxl
import json
#send request GET object to APEX
import requests
import time

class Golstats_jugador():

    # name made in constructor
    def __init__(self, filename,jornada_id):
        self.excel = filename
        self.token = {}
        self.jornada_id = jornada_id
        #Header = 5 because is the row position of the names
        self.h = 5


    def brute_force(self,nombre):

        if nombre == 'Mancuello, Federico Andres':
            return 'FEDERICO MANCUELLO'

        if nombre == 'Zago Gavito, Diego':
            return 'DIEGO ZAGO'

        if nombre == 'Cortizo de la Piedra, Jordi':
            return 'JORDI CORTIZO'


        if nombre == 'Ramirez Dutra, Kevin':
            return 'KEVIN RAMIREZ'

        if nombre == 'Barragan Negrete, Martin':
            return 'MARTIN BARRAGAN'

        if nombre == 'Villalpando Perez, Dieter':
            return 'DIETER VILLALPANDO'

        if nombre == 'Castillo Gonzalez, Raul':
            return 'RAUL CASTILLO'

        if nombre == 'Martinez Gonzalez, Emilio':
            return 'EMILIO MARTINEZ'

        if nombre == 'Juarez Del Castillo, Ramon':
            return 'RAMON JUAREZ'

        if nombre == 'Vazquez Serrano, Ivo':
            return 'IVO VAZQUEZ'

        if nombre == 'Robles Guerrero, Angel':
            return 'ANGEL ROBLES'

        if nombre == 'Aboagye, Clifford':
            return 'CLIFFORD ABOAGYE'

        if nombre == 'Alvarez Lopez, Daniel':
            return 'DANIEL ALVAREZ'

        if nombre == 'Aguilar Munoz, Daniel ':
            return 'DANIEL AGUILAR'

        if nombre == 'Araujo Vilches, Maximiliano':
            return 'MAXIMILIANO ARAÚJO'

        if nombre == 'Aristeguieta de Luca, Fernando':
            return 'FERNANDO ARISTEGUIETA'

        if nombre == 'Corral Ang, George':
            return 'GEORGE CORRAL'

        if nombre == 'De Buen Juarez, Diego':
            return 'DIEGO DE BUEN'

        if nombre == 'Escoto Ruiz, Amaury':
            return 'AMAURY ESCOTO'

        if nombre == 'Ferrareis, Gustavo Henrique':
            return 'GUSTAVO FERRAREIS'

        if nombre == 'Gularte Mendez, Emanuel':
            return 'EMANUEL GULARTE'

        if nombre == 'Herrera Rodriguez, Alberto':
            return 'ALBERTO HERRERA'

        if nombre == 'Jaques Varone Maia, Lucas':
            return 'LUCAS MAIA'

        if nombre == 'Parra Rubilar, Pablo':
            return 'PABLO PARRA'

        if nombre == 'Reyes Romero, Israel':
            return 'ISRAEL REYES'

        if nombre == 'Salas Salazar, Javier':
            return 'JAVIER SALAS'

        if nombre == 'Segovia Gonzalez, Juan':
            return 'JUAN SEGOVIA'

        if nombre == 'Tabo Hornos, Christian':
            return 'CHRISTIAN TABO'

        if nombre == 'Martinez Ayala, Guillermo':
            return 'GUILLERMO MARTÍNEZ'

        return None


    def fill_golstats(self):
        #Se llena un hashtable con los jugadores que participaron en la sesion

        require_cols_sheet_0 = [0,5,40,85,90,95,96]

        dataframe = pd.read_excel(self.excel,header = self.h ,usecols = require_cols_sheet_0)
        full_name = []
        for index, row in dataframe.iterrows():
            row_name = row['Nombre']
            name = self.brute_force(row_name)
            if name == None:
                print(row)
                sys.exit()
            else:
                full_name.append(name)

        dataframe['Nombre']=full_name

        return dataframe

    def crear_jugador_jornada(self):
        #endpoint request get_url
        jugador_jornada_post  = 'https://g6d5f1265b0dcaf-dbapex.adb.us-ashburn-1.oraclecloudapps.com/ords/db_apex/jornada/jugador_jornada'

        #Obtener los datos de distancia de wimu
        df = self.fill_golstats()
        #Obtener los hse de wimu

        #Obtener los datos de sprints de wimu
        print(df)

        isContained = False


        counter= 1
        #   #   Obtener el torneo en donde insertae del endpoint    #  #
        for index, row in df.iterrows():
            data = {
                "jugador":row[0],
                "minutos_jugados": row[1],
                "goles_anotados": row[2],
                "faltas_cometidas": row[3],
                "faltas_recibidas": row[4],
                "tarjetas_amarillas": row[5],
                "tarjetas_rojas":row[6],
                "id_jornada":self.jornada_id
            }
            api_call_sesion_response = requests.post(jugador_jornada_post, params = data,verify=False)
            #api_call_sesion_response = requests.post(url_jugador_sesion, headers=api_call_headers, params = data,verify=False)
            print(counter, ".- ", api_call_sesion_response.status_code)
            counter = counter + 1
            #Row[1] = columna de goles, solo si el jugador ha anotado goles se agregara al  jugador_sesion previamente creado
        return True


    def post_golstats_posicion(self,items):
        #Obtener todos los valores de jugador x jornada

        #Se llena un hashtable con los jugadores que participaron en la sesion
        """
        pases_acertados_cancha_propia: 6
        pases_no_acertados_cancha_propia: 9
        pases_acertados_cancha_rival: 12
        pases_no_acertados_cancha_rival: 15
        balones_recuperados_disputa: 19
        balones_perdidos_disputa: 22
        rechaces: 24
        uno_vs_uno_exitoso_ofensivo: 25
        uno_vs_uno_no_exitoso_ofensivo: 26
        uno_vs_uno_exitoso_defensivo: 27
        uno_vs_uno_no_exitoso_defensivo: 28
        area_rival:33
        balones_ganados_area_propia: 36
        asistencias: 46
        tiro_gol: 48
        centros_izquierda: 52
        centros_derecha: 57

        """
        require_cols_sheet_0 = [0,6,9,12,15,19,22,24,25,26,27,28,33,36,46,48,52,57]

        dataframe = pd.read_excel(self.excel,header = self.h ,usecols = require_cols_sheet_0)
        full_name = []
        for index, row in dataframe.iterrows():
            row_name = row['Nombre']
            name = self.brute_force(row_name)
            if name == None:
                print(row)
                sys.exit()
            else:
                full_name.append(name)

        dataframe['Nombre']=full_name
        print(dataframe)
            #Postear cada estadistica en cada posicion del jugador
        counter= 1
        #   #   Obtener el torneo en donde insertae del endpoint    #  #
        for index, row in dataframe.iterrows():
            for i in items:
                if i['wimu_alias'] == row[0]:
                    id_jugador_jornada = i['jugador_jornada_id']
                    print(i['wimu_alias'] , id_jugador_jornada)
                    break
            data = {
                "pacr": row[3],
                "pnacr": row[4],
                "brd": row[5],
                "bpd": row[6],
                "pacp": row[1],
                "pnacp": row[2],
                "uno_vs_uno_exdef": row[10],
                "uno_vs_uno_no_exdef": row[11],
                "uno_vs_uno_exof": row[8],
                "uno_vs_uno_no_exof": row[9],
                "area_rival": row[12],
                "rechaces": row[7],
                "asistencias": row[14],
                "bgap": row[13],
                "centros_izquierda": row[16],
                "centros_derecha": row[17],
                "tiro_gol": row[15],
                "id_jugador_jornada":id_jugador_jornada

            }
            url_golstats_jugador_posicion = "https://g6d5f1265b0dcaf-dbapex.adb.us-ashburn-1.oraclecloudapps.com/ords/db_apex/golstats/posicion_golstats"

            api_call_sesion_response = requests.post(url_golstats_jugador_posicion, params = data,verify=False)
            #api_call_sesion_response = requests.post(url_jugador_sesion, headers=api_call_headers, params = data,verify=False)
            print(counter, ".- ", api_call_sesion_response.status_code)
            counter = counter + 1
            #Row[1] = columna de goles, solo si el jugador ha anotado goles se agregara al  jugador_sesion previamente creado

        return dataframe
