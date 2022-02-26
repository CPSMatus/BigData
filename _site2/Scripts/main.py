from jornada_dataframe import Jornada
#from mean_team import Mean_team
from sum_player_jornada import Mean_player_jornada
from mean_team_jornada import Mean_team_jornada
from mean_team_minuto import Mean_team_minuto
import pandas as pd
import numpy as np
import openpyxl
import numpy as np
import matplotlib.pyplot as plt
# Program extracting first column

import seaborn as sns
import time
import xlrd

global excel
global hse_sheet
global require_cols_sheet_1
global jornadas_array

global require_cols_sheet_3
require_cols_sheet_1 = [0,3,4,16,17,18]
require_cols_sheet_3 = [0,3]
loc = ("/Users/smatus/Desktop/Club Puebla/Excel Jornadas/")
jornadas_array = ["J01 MONTERREY VS PUEBLA",
                "J02 GUADALAJARA VS PUEBLA",
                "J03 AMERICA VS PUEBLA",
                "J04 TIGRES VS PUEBLA",
                "J05 TIJUANA VS PUEBLA",
                "J06 PUMAS VS PUEBLA",
                "J07 QUERETARO VS PUEBLA",
                "J08 SAN LUIS VS PUEBLA",
                "J09 SANTOS VS PUEBLA",
                "J10 CRUZ AZUL VS PUEBLA",
                "J11 ATLAS VS PUEBLA",
                "J12 PACHUCA VS PUEBLA",
                "J13 NECAXA VS PUEBLA",
                "J14 MAZATLAN VS PUEBLA",
                "J15 LEON VS PUEBLA",
                "J16 JUAREZ VS PUEBLA",
                "J17 TOLUCA VS PUEBLA"]
hse_sheet = 3


jornadas_hash_table = {}
players_hash_table = {}
players = []

#Incluir tambien en el template del servidor

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


def select_jugador():
    players_array = np.array(["AMAURY ESCOTO",
                                "ANGEL ROBLES",
                                "CRISTIAN TABO",
                                "CRISTIAN MARES",
                                "DANIEL AGUILAR",
                                "DANIEL ALVAREZ",
                                "DIEGO DE BUEN",
                                "EMANUEL GULARTE",

                                "FERNANDO ARISTEGUIETA",
                                "GEORGE CORRAL",
                                "GUSTAVO FERRAREIS",
                                "ISRAEL REYES",
                                "IVO VAZQUEZ",
                                "JAVIER SALAS",
                                "JHORY CELAYA",
                                "JUAN SEGOVIA",

                                "LUCAS MAIA",
                                "MAXIMILIANO ARAUJO",
                                "PABLO PARRA",
                                "RAUL CASTILLO"
                                ])
    for i in range(9):
        players_hash_table[i] = players_array[i]

    print("Selecciona el jugador a analizar")


def select_jornada():
    global int_game
    for i in range(len(jornadas_excel_array)):
        jornadas_hash_table[i] = jornadas_excel_array[i]

    print("Selecciona la jornada a analizar ")

    for i in jornadas_array:
        print (i)

    int_game = int(input())
    string_game = jornadas_hash_table[int_game-1]
    return string_game


#selected_player = selected_player()
#print(selected_player)

selected_jornada = select_jornada()
print("\nJORNADA SELECCIONADA, ", selected_jornada)

#crear eje x
minutes_interval = Jornada.send_minutes_interval()
#seleccionar al jugador a evaluar
selected_player = Jornada.select_player(selected_jornada)
#start time count
inicio = time.time()
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


distance = pd.DataFrame({ "Distance" : distance_array,
                        "type" : "Distance (m)",
                        "Minutes" : minutes_interval })

distance_high_intensity = pd.DataFrame({ "Distance" : high_intensity_distance_array,
                        "type" : "Distance (m)",
                        "Minutes" : minutes_interval })

sprint_abs_cnt = pd.DataFrame({ "Sprints" : sprint_abs_cnt_array,
                        "type" : " Sprints",
                        "Minutes" : minutes_interval })


# Initialise the subplot function using number of rows and columns
figure, axis = plt.subplots(2, 2)

figure.suptitle(selected_player)

axis[0,0].plot(distance['Minutes'], distance['Distance'])
axis[0,0].set_title("Distancia (m)")
axis[0,0].grid()

axis[0,1].plot(distance_high_intensity['Minutes'], distance_high_intensity['Distance'])
axis[0,1].set_title("Distancia Alta Intensidad(m)")
axis[0,1].grid()

axis[1,0].plot(sprint_abs_cnt['Minutes'], sprint_abs_cnt['Sprints'])
axis[1,0].set_title("Sprints")
axis[1,0].grid()



#enviamos las jornadas al eje x
x_mean_interval = Mean_player_jornada.set_x_range()

#Analisis jugador x Jornada
distance_array_mean = Mean_player_jornada.select_distance_values(jornadas_excel_array,selected_player)

high_intensity_distance_array_mean = Mean_player_jornada.select_high_intensity_distance_values(jornadas_excel_array, selected_player)

sprint_abs_cnt_array_mean = Mean_player_jornada.select_sprint_abs_cnt_values(jornadas_excel_array, selected_player)


#Construction pandas dataframe for player Jornada
distance_mean = pd.DataFrame({ "Distance" : distance_array_mean,
                        "type" : "Distance (m)",
                        "Jornadas" : x_mean_interval })

distance_high_intensity_mean = pd.DataFrame({ "Distance" : high_intensity_distance_array_mean,
                        "type" : "Distance (m)",
                        "Jornadas" : x_mean_interval })


sprint_abs_cnt_mean = pd.DataFrame({ "Sprints" : sprint_abs_cnt_array_mean,
                        "type" : " Sprints",
                        "Jornadas" : x_mean_interval })

# Graficas de Jugador por jornada
figure2, axis2 = plt.subplots(2, 2)
string_figure2 =  selected_player + "\nTORNEO "
figure2.suptitle(string_figure2)

axis2[0,0].plot(distance_mean['Jornadas'], distance_mean['Distance'])
axis2[0,0].set_title("Distancia (m)")
axis2[0,0].grid()

axis2[0,1].plot(distance_high_intensity_mean['Jornadas'], distance_high_intensity_mean['Distance'])
axis2[0,1].set_title("Distancia Promedio Alta Intensidad (m)")
axis2[0,1].grid()


axis2[1,0].plot(sprint_abs_cnt_mean['Jornadas'], sprint_abs_cnt_mean['Sprints'])
axis2[1,0].set_title("Sprints")
axis2[1,0].grid()


#Analisis del Equipo por Minuto
players_hash_table = Jornada.fill_players(selected_jornada)

distance_array_mean_team2 = Mean_team_minuto.select_distance_team_values(players_hash_table,frames)

#print("ARRAY RESULT FROM MAIN", distance_array_mean_team2)
sprint_abs_cnt_array_mean_team = Mean_team_minuto.select_sprints_team_values(players_hash_table,frames)

hi_distance_array_mean_team = Mean_team_minuto.select_high_intensity_team_values(players_hash_table,frames)
#print(hi_distance_array_mean_team)

#Construction pandas dataframe for team average
distance_mean_team2 = pd.DataFrame({ "Distance" : distance_array_mean_team2,
                        "type" : "Distance (m)",
                        "Minutes" : minutes_interval})

#print("ARRAY RESULT", distance_mean_team2['Distance'])

sprint_abs_cnt_mean_team = pd.DataFrame({ "Sprints" : sprint_abs_cnt_array_mean_team,
                        "type" : " Sprints" ,
                        "Minutes" : minutes_interval})


distance_hi_mean_team = pd.DataFrame({ "Distance" : hi_distance_array_mean_team,
                        "type" : "Distance (m)",
                        "Minutes" : minutes_interval })
#print(distance_hi_mean_team['Distance'])


# Initialise the subplot function using number of rows and columns
figure4, axis4 = plt.subplots(2, 2)
figure4.suptitle("Promedio del equipo\n" + jornadas_array[int_game-1])
axis4[0,0].plot(distance['Minutes'], distance_array_mean_team2)
axis4[0,0].set_title("Distancia (m)")
axis4[0,0].grid()


axis[1,1].plot(distance['Minutes'], distance['Distance'] ,label = "Distance (m)")
axis[1,1].plot(distance['Minutes'], distance_array_mean_team2, label = "Avg Distance")
axis[1,1].set_title("Distancia(m) vs Distancia Promedio Equipo")
axis[1,1].legend()

axis4[1,0].plot(sprint_abs_cnt['Minutes'], sprint_abs_cnt_mean_team['Sprints'])
axis4[1,0].set_title("Sprints")
axis4[1,0].grid()


axis4[0,1].plot(distance_hi_mean_team['Minutes'], distance_hi_mean_team['Distance'])
axis4[0,1].set_title("Distancia Alta Intensidad(m)")
axis4[0,1].grid()





##Arrays for team x Jornada
distance_array_mean_jornada = Mean_team_jornada.select_distance_values(jornadas_excel_array)

hi_distance_array_mean_jornada = Mean_team_jornada.select_high_intensity_distance_values(jornadas_excel_array)

sprint_abs_cnt_array_mean_jornada = Mean_team_jornada.select_sprint_abs_cnt_values(jornadas_excel_array)




fin = time.time()
print("Without plot: ",fin-inicio)



#Construction pandas dataframe for team x Jornada
distance_team_jornada = pd.DataFrame({ "Distance" : distance_array_mean_jornada,
                        "type" : "Distance (m)",
                        "Jornadas" : x_mean_interval })


# Graficas del equipo por jornada
figure3, axis3 = plt.subplots(2, 2)
string_figure3 =  "Analisis del Equipo \n Durante el Torneo"
figure3.suptitle(string_figure3)


axis3[0,0].plot(distance_team_jornada['Jornadas'], distance_team_jornada['Distance'])
axis3[0,0].set_title("Distance (m)")
axis3[0,0].grid()


distance_hi_team_jornada = pd.DataFrame({ "Distance" : hi_distance_array_mean_jornada,
                        "type" : "Distance (m)",
                        "Jornadas" : x_mean_interval })


axis3[0,1].plot(distance_hi_team_jornada['Jornadas'], distance_hi_team_jornada['Distance'])
axis3[0,1].set_title("Distancia en alta intensidad")
axis3[0,1].grid()




sprint_abs_cnt_team_jornada = pd.DataFrame({ "Sprints" : sprint_abs_cnt_array_mean_jornada,
                        "type" : " Sprints",
                        "Jornadas" : x_mean_interval })




axis3[1,0].plot(sprint_abs_cnt_team_jornada['Jornadas'], sprint_abs_cnt_team_jornada['Sprints'])
axis3[1,0].set_title("Sprints")
axis3[1,0].grid()





plt.show()
