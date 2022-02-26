#import excel_execution
import numpy as np
from jornada_dataframe import Jornada

class Mean_player_jornada():

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

    def sum(array):
        sum = 0
        for i in array:
            sum = sum + int(i)
        return sum


    def select_distance_values(jornadas_array, selected_player):

        sum_distance_array = []
        mean = 0
        for i in jornadas_array:
            #Obtenemos todos los valores de cada jornada
            #Extraer las columnas del excel para analizar solo el dataframe
            result = Jornada.create_df(i)
            #Obtener los lapsos a examinar, eliminar drills y primer tiempo
            frames = Jornada.create_df_parameters(result)
            #Obtener la distance(m)
            distance_array = Jornada.get_distance_for_player(selected_player,frames)
            #sumamos todos los valores
            total = Mean_player_jornada.sum(distance_array)
            sum_distance_array.append(total)

        #Llenamos con zeros el resto de las jornadas no jugadas
        for i in range(len(sum_distance_array), 17):
            sum_distance_array.append(0)
        return sum_distance_array

    def select_high_intensity_distance_values(jornadas_array, selected_player):

        sum_hi_distance_array = []
        mean = 0
        for i in jornadas_array:
            #Obtenemos todos los valores de cada jornada
            #Extraer las columnas del excel para analizar solo el dataframe
            result = Jornada.create_df(i)
            #Obtener los lapsos a examinar, eliminar drills y primer tiempo
            frames = Jornada.create_df_parameters(result)
            #Obtener la distance(m)
            distance_array = Jornada.get_high_intensisty_distance_for_player(selected_player,frames)
            #calculamos el promedio y lo agregamos a la variable retornada
            total = Mean_player_jornada.sum(distance_array)
            sum_hi_distance_array.append(total)

        #Llenamos con zeros el resto de las jornadas no jugadas
        for i in range(len(sum_hi_distance_array), 17):
            sum_hi_distance_array.append(0)
        return sum_hi_distance_array

    def select_sprint_abs_cnt_values(jornadas_array, selected_player):

        sum_sprints_array = []
        mean = 0
        for i in jornadas_array:
            #Obtenemos todos los valores de cada jornada
            #Extraer las columnas del excel para analizar solo el dataframe
            result = Jornada.create_df(i)
            #Obtener los lapsos a examinar, eliminar drills y primer tiempo
            frames = Jornada.create_df_parameters(result)
            #Obtener la distance(m)
            sprints_array = Jornada.get_sprints_for_player(selected_player,frames)
            #calculamos el promedio y lo agregamos a la variable retornada
            total = Mean_player_jornada.sum(sprints_array)
            sum_sprints_array.append(total)

        #Llenamos con zeros el resto de las jornadas no jugadas
        for i in range(len(sum_sprints_array), 17):
            sum_sprints_array.append(0)

        return sum_sprints_array
