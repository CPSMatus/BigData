#import excel_execution
import numpy as np
from jornada_dataframe import Jornada
from mean_team_minuto import Mean_team_minuto

class Mean_team_jornada():

    jornadas_hash_table = {}
    def set_x_range():
        x_range = np.array(["J01",
                            "J02",
                            "J03",
                            "J04",
                            "J05",
                            "J06",
                            "J07",
                            "J08",
                            "J09",
                            "J10",
                            "J11",
                            "J12",
                            "J13",
                            "J14",
                            "J15",
                            "J16",
                            "J17"
                            ])
        return x_range

    def sum(values,array):
        for i in range(len(values)):
            values[i] = float(values[i]) + float(array[i])
        return values


    def define_mean(array):
        sum = 0.0
        for i in array:
            sum = sum + i
        mean = float(sum)
        #print("\n",sum)
        #print("\n", mean)
        return mean


    def select_distance_values(jornadas_array):

        mean_distance_array = []
        mean = 0.0
        for i in jornadas_array:
            print("\n",i)
            #Obtenemos todos los valores de cada jornada
            #Extraer las columnas del excel para analizar solo el dataframe
            result = Jornada.create_df(i)
            #Obtener los lapsos a examinar, eliminar drills y primer tiempo
            frames = Jornada.create_df_parameters(result)
            players_hash_table = Jornada.fill_players(i)

            #calculamos el promedio y lo agregamos a la variable retornada
            mean_by_minuto = Mean_team_minuto.select_distance_team_values(players_hash_table,frames)
            #print(mean_by_minuto)
            mean = Mean_team_jornada.define_mean(mean_by_minuto)
            mean_distance_array.append(mean)
            #print(mean_by_minuto)
        #Llenamos con zeros el resto de las jornadas no jugadas
        for i in range(len(mean_distance_array), 17):
            mean_distance_array.append(0)
        #print(mean_distance_array)
        return mean_distance_array
 


    def select_high_intensity_distance_values(jornadas_array):

        mean_hi_distance_array = []
        mean = 0.0
        for i in jornadas_array:
            print("HSE \n",i)
            #Obtenemos todos los valores de cada jornada
            #Extraer las columnas del excel para analizar solo el dataframe
            result = Jornada.create_df(i)
            #Obtener los lapsos a examinar, eliminar drills y primer tiempo
            frames = Jornada.create_df_parameters(result)
            #Obtener la distance(m)
            #Obtener la lista de todos los jugadores
            players_hash_table = Jornada.fill_players(i)
            #calculamos el promedio y lo agregamos a la variable retornada
            mean_by_minuto = Mean_team_minuto.select_high_intensity_team_values(players_hash_table,frames)

            mean = Mean_team_jornada.define_mean(mean_by_minuto)
            mean_hi_distance_array.append(mean)

        #Llenamos con zeros el resto de las jornadas no jugadas
        for i in range(len(mean_hi_distance_array), 17):
            mean_hi_distance_array.append(0)
        return mean_hi_distance_array

    def select_sprint_abs_cnt_values(jornadas_array):

        mean_sprints_array = []
        mean = 0.0
        for i in jornadas_array:
            print("SPRINTS \n",i)
            #Obtenemos todos los valores de cada jornada
            #Extraer las columnas del excel para analizar solo el dataframe
            result = Jornada.create_df(i)
            #Obtener los lapsos a examinar, eliminar drills y primer tiempo
            frames = Jornada.create_df_parameters(result)
            #Obtener la distance(m)
            #Obtener la lista de todos los jugadores
            players_hash_table = Jornada.fill_players(i)

            #calculamos el promedio y lo agregamos a la variable retornada
            mean_by_minuto = Mean_team_minuto.select_sprints_team_values(players_hash_table,frames)
            #print(mean_by_minuto)
            mean = Mean_team_jornada.define_mean(mean_by_minuto)
            mean_sprints_array.append(mean)


        #Llenamos con zeros el resto de las jornadas no jugadas
        for i in range(len(mean_sprints_array), 17):
            mean_sprints_array.append(0)

        return mean_sprints_array
