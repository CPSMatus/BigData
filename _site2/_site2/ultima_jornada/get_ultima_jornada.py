import json
import requests
import pandas as pd
import json

class Ultima_Jornada():

    def get_jornada_info(self):

        #endpoint request get_url
        test_api_url  = 'https://g6d5f1265b0dcaf-dbapex.adb.us-ashburn-1.oraclecloudapps.com/ords/db_apex/jornada/ultima_jornada'

        api_call_response = requests.get(test_api_url)

        #   #   Obtener la JORNADA  en donde se insertara el endpoint    #  #

        if	api_call_response.status_code == 401:
        	token = get_new_token()
        else:
            items = api_call_response.json()
        return items['items'][0]

    def get_jornada_id(self):

        #    #    #    #     GET THE ID DE LA ULTIMA JORNADA     #    #   #  #


        #endpoint request get_url
        test_api_url  = 'https://g6d5f1265b0dcaf-dbapex.adb.us-ashburn-1.oraclecloudapps.com/ords/db_apex/jornada/ultima_jornada'

        api_call_response = requests.get(test_api_url)

        #   #   Obtener la JORNADA  en donde se insertara el endpoint    #  #

        if	api_call_response.status_code == 401:
        	token = get_new_token()
        else:
            items = api_call_response.json()

        jornada_id_num = (int) (items['items'][0]['jornada_id'])

        return jornada_id_num

    def get_jornada_wimu_info(self):

        id_jornada = self.get_jornada_id()
        #endpoint request get_url
        test_api_url  = 'https://g6d5f1265b0dcaf-dbapex.adb.us-ashburn-1.oraclecloudapps.com/ords/db_apex/jornada/uj_wimu_info'

        data = {
            'id_jornada' :id_jornada
        }

        api_call_response = requests.get(test_api_url, params = data)

        #   #   Obtener la JORNADA  en donde se insertara el endpoint    #  #

        if	api_call_response.status_code == 401:
        	token = get_new_token()
        else:
            items = api_call_response.json()

        return items

    def get_rival_info(self):
        #Obtenemos la ultima jornada
        jornada = self.get_jornada_info()
        id_rival = (int) (jornada['items'][0]['id_rival'])

        test_api_url  = 'https://g6d5f1265b0dcaf-dbapex.adb.us-ashburn-1.oraclecloudapps.com/ords/db_apex/general/equipo'

        data = {
            'equipo_id' :id_rival
        }

        api_call_response = requests.get(test_api_url, params = data)

        #   #   Obtener la JORNADA  en donde se insertara el endpoint    #  #

        if	api_call_response.status_code == 401:
        	token = get_new_token()
        else:
            items = api_call_response.json()

        return items['items'][0]




    def get_table(self):
        response = self.get_jornada_wimu_info()
        sum_distance = 0.0
        sum_hse = 0.0
        sum_sprints = 0
        #put on an array all the elements of the Distance per player


        array = []

        for i in response['items']:
            posicion = i['nombre_posicion']
            id_jugador_jornada = i['jugador_jornada_id']
            id_jugador = i['id_jugador']
            sum_distance = 0.0
            sum_hse = 0.0
            sum_sprints = 0
            #Cambiar los nombres
            name = self.change_mayus(i['wimu_alias'])

            #Agregar los minutos jugados
            minutos_jugados = i['minutos_jugados']

            #Sumar todas las distancias
            sum_distance += i['distance_0_10']
            sum_distance += i['distance_10_20']
            sum_distance += i['distance_20_30']
            sum_distance += i['distance_30_40']
            sum_distance += i['distance_40_45']
            sum_distance += i['distance_45_50']
            sum_distance += i['distance_50_60']
            sum_distance += i['distance_60_70']
            sum_distance += i['distance_70_80']
            sum_distance += i['distance_80_90']
            sum_distance = round(sum_distance,2)
                #Sumar todas las hse
            sum_hse += i['hse_0_10']
            sum_hse += i['hse_10_20']
            sum_hse += i['hse_20_30']
            sum_hse += i['hse_30_40']
            sum_hse += i['hse_40_45']
            sum_hse += i['hse_45_50']
            sum_hse += i['hse_50_60']
            sum_hse += i['hse_60_70']
            sum_hse += i['hse_70_80']
            sum_hse += i['hse_80_90']
            sum_hse = round(sum_hse,2)

            #Sumar todoss los sprints
            sum_sprints += i['sprints_0_10']
            sum_sprints += i['sprints_10_20']
            sum_sprints += i['sprints_20_30']
            sum_sprints += i['sprints_30_40']
            sum_sprints += i['sprints_40_45']
            sum_sprints += i['sprints_45_50']
            sum_sprints += i['sprints_50_60']
            sum_sprints += i['sprints_60_70']
            sum_sprints += i['sprints_70_80']
            sum_sprints += i['sprints_80_90']

            #Agregar los metros minutos
            m_min = sum_distance / minutos_jugados
            m_min_2 = round(m_min,2)
            d = {'id_jugador_jornada':id_jugador_jornada,'id_jugador':id_jugador,'wimu_alias': name,'pos':posicion , 'minutos_jugados': minutos_jugados,
            'distance':sum_distance,'hse':sum_hse, 'sprints':sum_sprints,'m_min':m_min_2}

            array.append(d)

        return array

    def change_mayus(self,name):
        names_array = name.split()
        position = 0
        final_name = ""

        for i in names_array:
            firt_letter = i[0]
            i = i.lower()
            i = i[:position] + firt_letter + i[position+1:]
            final_name += i + " "
            #print(i)


        return final_name

    def get_jugadores(self):

        #    #    #    #     GET THE ID DE LA ULTIMA JORNADA     #    #   #  #
        id_jornada = self.get_jornada_id()
        #endpoint request get_url
        test_api_url  = 'https://g6d5f1265b0dcaf-dbapex.adb.us-ashburn-1.oraclecloudapps.com/ords/db_apex/jornada/jugadores_jornada'
        data = {
            'id_jornada' :id_jornada
        }

        api_call_response = requests.get(test_api_url, params = data)

        #   #   Obtener la JORNADA  en donde se insertara el endpoint    #  #

        if	api_call_response.status_code == 401:
        	token = get_new_token()
        else:
            items = api_call_response.json()

        return items

    def get_fecha_y_hora(self,string):

        string_array = string.split('T')

        array_hora = string_array[1].split('Z')

        d = {'fecha': string_array[0],'hora':array_hora[0] }
        print(d)
