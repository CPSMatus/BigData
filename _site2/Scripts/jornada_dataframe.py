import pandas as pd
import numpy as np
import openpyxl
import numpy as np
import matplotlib.pyplot as plt
import time
# Program extracting first column

import seaborn as sns

import xlrd

class Jornada():
    global loc

    global duration_cell_number
    global sheet
    global loc
    global require_cols_sheet_1
    global require_cols_sheet_3
    require_cols_sheet_1 = [0,4,16,17,18]
    require_cols_sheet_3 = [0,3]

    # name made in constructor
    def __init__(self,wimu_excel):
        self.wimu_excel = wimu_excel
        self.token = {}


    def create_df(self):

        hse_sheet = 3
        row = []
        #adding one row to put them in the same position
        row.insert(0,{'Player':0,'Sprint Abs Cnt':0})
        #reading hse excel
        r =  pd.read_excel(self.wimu_excel, sheet_name = hse_sheet, usecols = require_cols_sheet_3)
        #inserting one empty row
        hse_df = pd.concat([pd.DataFrame(row), r], ignore_index=True)
        #reading distance excel
        distance_df = pd.read_excel(self.wimu_excel, usecols = require_cols_sheet_1)
        #appending the two frames together
        df3 = [distance_df,hse_df["Sprint Abs Cnt"]]
        df_result = pd.concat(df3, axis = 1, sort = False)

        return df_result

    def send_minutes_interval():

        minutes_interval = np.array(["0-10",
                                    "10-20",
                                    "20-30",
                                    "30-40",
                                    "40-45",

                                    "45-50",
                                    "50-60",
                                    "60-70",
                                    "70-80",
                                    "80-90"
                                    ])

        return minutes_interval


    def print_jugadores(players_hash_table):
        for i in range(1,len(players_hash_table)+1):
            print(i ," ",players_hash_table[i])
        print("JUGARON EN TOTAL: ",len(players_hash_table))

    def fill_players(self):
        players_hash_table = {}
        n_players = 1
        isContained = False
        dataframe = pd.read_excel(self.wimu_excel, usecols = require_cols_sheet_1)
        dataframe = dataframe.dropna()
        #cuantos jugaron todo el partido
        for index, row in dataframe.iterrows():
            for a in range(1,len(players_hash_table)):
                if players_hash_table[a] ==  row["Player"]:
                    isContained = True
            if isContained == True:
                break
            #print(n_players , row["Player"] )
            players_hash_table[n_players] = row["Player"]
            n_players = n_players + 1

        return players_hash_table

    def select_player(self):
        players_hash_table = self.fill_players()
        Jornada.print_jugadores(players_hash_table)
        player_int = int(input())
        selected_player = players_hash_table[player_int]
        return selected_player

    def create_df_parameters(self,df):
        counter = 0

        for index, row in df.iterrows():
            if (row["Player"] == "0  10"):
                lap0_from = counter
            if (row["Player"] == "10  20"):
                lap0_to = counter
                lap1_from = counter
            if (row["Player"] == "20  30"):
                lap1_to = counter
                lap2_from = counter
            if (row["Player"] == "30  40"):
                lap2_to = counter
                lap3_from = counter
            if (row["Player"] == "40  50"):
                lap3_to = counter
                lap4_from = counter
            if (row["Player"] == "SEGUNDO TIEMPO"  ):
                lap4_to = counter

            if (row["Player"] == "0  5"):
                lap5_from = counter
            if (row["Player"] == "5  10"):
                lap5_to = counter
                lap6_from = counter
            if (row["Player"] == "15  20"):
                lap6_to = counter
                lap7_from = counter
            if (row["Player"] == "25  30"):
                lap7_to = counter
                lap8_from = counter
            if (row["Player"] == "35  40"):
                lap8_to = counter
                last_lap_from = counter
        # M I S S I N G   L A S T   L A P   E N D
            counter = counter + 1

        # CREATING SMALL SECTIONS OF DATAFRAME
        array  = [0] * 10

        df_lap0 = df.iloc[lap0_from:lap0_to,:]
        array[0] = df_lap0
        df_lap1 = df.iloc[lap1_from:lap1_to,:]
        array[1] = df_lap1
        df_lap2 = df.iloc[lap2_from:lap2_to,:]
        array[2] = df_lap2
        df_lap3 = df.iloc[lap3_from:lap3_to,:]
        array[3] = df_lap3
        df_lap4 = df.iloc[lap4_from:lap4_to,:]
        array[4] = df_lap4
        df_lap5 = df.iloc[lap5_from:lap5_to,:]
        array[5] = df_lap5
        df_lap6 = df.iloc[lap6_from:lap6_to,:]
        array[6] = df_lap6
        df_lap7 = df.iloc[lap7_from:lap7_to,:]
        array[7] = df_lap7
        df_lap8 = df.iloc[lap8_from:lap8_to,:]
        array[8] = df_lap8
        df_lap9 = df.iloc[last_lap_from:,:]
        array[9] = df_lap9
        return array




    def get_distance_for_player(player,array):
        array_result = [0.0] * 10
        counter = 0
        result = 0.0
        #Selecting all the values of the player by each laps
        for i in array:
            df = i.loc[i["Player"] == player, "Distance(m)"]
            if not df.empty:
                #Si el df no esta vacio, se cambiara el valor del arreglo por el
                #resultado arrojado por el df.
                if len(df) > 1:
                    #Si la longitud del df es mayor a 1, el jugador ha estado en
                    #2 lapsos de 5 min o mas, se sumaran esos valores
                    for row in df:
                        result = float(result) + float(row)
                        result_2 = round(result, 2)
                        array_result[counter] = result_2
                    result = 0.0
                else:
                    #append to the array only the distance value
                    array_result[counter] = float(df)
            counter = counter + 1

        return array_result


    def get_high_intensisty_distance_for_player(player,array):

        array_result = [0.0] * 10
        columns = ["Unnamed: 16","Unnamed: 17","Unnamed: 18"]
        counter = 0
        result = 0.0

        #Selecting all the values of the player by each laps
        for i in array:
            df = i.loc[i["Player"] == player, columns ]
            if not df.empty:
                #Si el df no esta vacio, se cambiara el valor del arreglo por el
                #resultado arrojado por el df.
                if len(df) > 1:
                    #Si la longitud del df es mayor a 1, el jugador ha estado en
                    #2 lapsos de 5 min o mas, se sumaran esos valores
                    sum = df[columns[0]] + df[columns[1]] + df[columns[2]]
                    for element in sum:
                        result = result + element
                    r = float(result)
                    result_2 = round(r, 2)
                    array_result[counter] = result_2
                    result = 0.0
                else:
                    #append to the array only the distance value
                    sum = df[columns[0]] + df[columns[1]] + df[columns[2]]
                    r = float(sum)
                    result_2 = round(r, 2)
                    array_result[counter] = result_2
                    sum = 0.0
            counter = counter + 1

        return array_result

    def get_sprints_for_player(player,array):
        array_result = [0.0] * 10
        counter = 0
        result = 0

        #Selecting all the values of the player by each laps
        for i in array:

            df = i.loc[i["Player"] == player, "Sprint Abs Cnt"]
            if not df.empty:
                #Si el df no esta vacio, se cambiara el valor del arreglo por el
                #resultado arrojado por el df.
                if len(df) > 1:
                    #Si la longitud del df es mayor a 1, el jugador ha estado en
                    #2 lapsos de 5 min o mas, se sumaran esos valores
                    for row in df:
                        result = result + row
                        array_result[counter] = result
                    result = 0
                else:
                    #append to the array only the distance value
                    array_result[counter] = int(df)
            counter = counter + 1
        return array_result
