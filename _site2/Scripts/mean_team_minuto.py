import numpy as np
from jornada_dataframe import Jornada
import pandas as pd
class Mean_team_minuto():

    global percentage
    percentage = 0.75

    def define_mean(total_array,array_player_counter):
        array_result = [0.0] * 10

        for i in range(10):
            array_result[i] = total_array[i] / array_player_counter[i]
        return array_result

    def define_armonic_mean(total_array,array_player_counter):
        array_pre_result = [0.0] * 10
        array_result = [0.0] * 10

        for i in range(10):
            array_pre_result[i] = 1 / total_array[i]

        for i in range(10):
                array_result[i] = array_player_counter[i]/array_pre_result[i]
        return array_result

    def count_players (time_array,array_player_counter):
        #print(time_array)
        for i in range(10):
            #get the 60 % of 00:09:59
            play_time = pd.Series("00:09:59")
            play_time = pd.to_timedelta(play_time)

            if ((i == 4) or (i==5)) :
                play_time = pd.Series("00:04:59")
                play_time = pd.to_timedelta(play_time)

            limit_time = (play_time / pd.offsets.Minute(1))
            if(float(time_array[i]) > float(limit_time)):
                #print("Play time", float(time_array[i]), " vs ", float(limit_time))
                #change the time
                limit_time = (time_array[i])

            #get the 60% of the limit
            limit_time = limit_time * percentage
            #print("LIMIT TIME IS: " , limit_time )


            if (float(time_array[i]) > float(limit_time)):
                #Add one to the player's array count if the time is bigger than
                #the 60%
                array_player_counter[i] = array_player_counter[i] + 1

        #print("\n",array_player_counter)
        return array_player_counter

    def count_armonic_players (time_array,array_player_counter):
        #print(time_array)
        for i in range(10):

            if (float(time_array[i]) != 0):
                #If the time is differente from 0, the player has being in the game
                array_player_counter[i] = array_player_counter[i] + 1

        #print("\n",array_player_counter)
        return array_player_counter

    def add_values(values_array,total_array):
        counter = 0
        #print("\n")
        for i in values_array:
            #add to the total sum the distance value
            #print(total_array[counter] ," + " , i , " = " , float(total_array[counter]) + float(i))
            total_array[counter] = float(total_array[counter]) + float(i)
            counter = counter + 1
        return total_array

    def get_distance_and_time_for_player(player,array):
        array_result = []
        array_distance =[0.0] * 10
        array_time = [0] * 10
        counter = 0
        time_sum = 0
        distance_sum = 0
        percentage = 0.75
        columns = ["Positioning Duration","Distance(m)"]
        result = 0

        #Selecting all the values of the player by each laps
        for i in array:
            df = i.loc[i["Player"] == player,columns ]
            if not df.empty:
                #Convert object time to float
                s = pd.Series(df[columns[0]])
                s = pd.to_timedelta(s)
                time_float = s / pd.offsets.Minute(1)
                if len(df) > 1:

                    for row in df[columns[1]]:
                        #add together the distance interval
                        distance_sum = distance_sum + row

                    for e in time_float:
                        #add together the time interval
                        time_sum = time_sum + e

                    #add the sum of the distance to the array
                    array_distance[counter] = (distance_sum)
                    array_time[counter] =  (time_sum)
                    #print("\n TIME SUM ",time_sum)
                    #print("\n DISTANCE SUM ",distance_sum)
                    distance_sum = 0
                    time_sum = 0
                else:
                    array_distance[counter] = float(df[columns[1]])
                    array_time[counter] = (time_float)


            counter = counter + 1
        #En la posicion 0 el tiempo
        array_result.append(array_time)
        #En la posicion 1 la distancia
        array_result.append(array_distance)
    #    print("ARRAY DISTANCE: ",array_distance)

        return array_result

    def get_sprints_and_time_for_player(player,array):
        array_result = []
        array_sprints =[0] * 10
        array_time = [0] * 10
        counter = 0
        time_sum = 0
        sprints_sum = 0
        percentage = 0.75
        columns = ["Positioning Duration","Sprint Abs Cnt"]
        result = 0

        #Selecting all the values of the player by each laps
        for i in array:
            df = i.loc[i["Player"] == player,columns ]
            if not df.empty:
                #Convert object time to float
                s = pd.Series(df[columns[0]])
                s = pd.to_timedelta(s)
                time_float = s / pd.offsets.Minute(1)
                if len(df) > 1:

                    for row in df[columns[1]]:
                        #add together the distance interval
                        sprints_sum = sprints_sum + row

                    for e in time_float:
                        #add together the time interval
                        time_sum = time_sum + e

                    #add the sum of the distance to the array
                    array_sprints[counter] = (sprints_sum)
                    array_time[counter] =  (time_sum)
                    #print("\n TIME SUM ",time_sum)
                    #print("\n DISTANCE SUM ",distance_sum)
                    sprints_sum = 0
                    time_sum = 0
                else:
                    array_sprints[counter] = float(df[columns[1]])
                    array_time[counter] = (time_float)


            counter = counter + 1
        #En la posicion 0 el tiempo
        array_result.append(array_time)
        #En la posicion 1 la distancia
        array_result.append(array_sprints)
        #    print("ARRAY DISTANCE: ",array_distance)
        return array_result

    def get_high_intensity_and_time_for_player(player,array):
        array_result = []
        array_hi_distance =[0] * 10
        array_time = [0] * 10
        counter = 0
        time_sum = 0
        sprints_sum = 0
        percentage = 0.75
        columns = ["Positioning Duration","Unnamed: 16","Unnamed: 17","Unnamed: 18"]
        result = 0

        #Selecting all the values of the player by each laps
        for i in array:
            df = i.loc[i["Player"] == player,columns ]
            if not df.empty:
                #Convert object time to float
                s = pd.Series(df[columns[0]])
                s = pd.to_timedelta(s)
                time_float = s / pd.offsets.Minute(1)

                if len(df) > 1:

                    for row in df[columns[1]]:
                        #add together the distance interval
                        sprints_sum = sprints_sum +  row

                    for row in df[columns[2]]:
                        #add together the distance interval
                        sprints_sum = sprints_sum +  row

                    for row in df[columns[3]]:
                        #add together the distance interval
                        sprints_sum = sprints_sum +  row

                    for e in time_float:
                        #add together the time interval
                        time_sum = time_sum + e

                    #add the sum of the distance to the array
                    array_hi_distance[counter] = (sprints_sum)
                    array_time[counter] =  (time_sum)
                    #print("\n TIME SUM ",time_sum)
                    #print("\n DISTANCE SUM ",distance_sum)
                    sprints_sum = 0
                    time_sum = 0
                else:
                    val = df[columns[1]] + df[columns[2]] + df[columns[3]]
                    array_hi_distance[counter] = float(val)
                    array_time[counter] = (time_float)


            counter = counter + 1
        #En la posicion 0 el tiempo
        array_result.append(array_time)
        #En la posicion 1 la distancia
        array_result.append(array_hi_distance)
        #    print("ARRAY DISTANCE: ",array_distance)
        return array_result


    def select_distance_team_values(players_hash_table,frames):

        total_array = [0.0] * 10
        array_results = [0.0] * 2
        array_player_counter = [0] * 10
        for i in range(1,len(players_hash_table)+1):

            array_results = Mean_team_minuto.get_distance_and_time_for_player(players_hash_table[i],frames)

            #time_sum = Mean_team_minuto.add_values(array_results[0],time_sum)
            #print("\n",players_hash_table[i])
            total_array = Mean_team_minuto.add_values(array_results[1],total_array)

            array_player_counter = Mean_team_minuto.count_players(array_results[0],array_player_counter)
            #print(array_player_counter)
        array_result = Mean_team_minuto.define_mean(total_array,array_player_counter)
        #print(array_result)
        return array_result

    def create_armonic_mean(players_hash_table,frames):

        total_array = [0.0] * 10
        array_results = [0.0] * 2
        array_player_counter = [0] * 10
        for i in range(1,len(players_hash_table)+1):

            array_results = Mean_team_minuto.get_distance_and_time_for_player(players_hash_table[i],frames)

            #time_sum = Mean_team_minuto.add_values(array_results[0],time_sum)
            #print("\n",players_hash_table[i])
            total_array = Mean_team_minuto.add_values(array_results[1],total_array)

            array_player_counter = Mean_team_minuto.count_armonic_players(array_results[0],array_player_counter)
        #    print(array_player_counter)
        array_result = Mean_team_minuto.define_armonic_mean(total_array,array_player_counter)
        #print(array_result)
        return array_result


    def select_sprints_team_values(players_hash_table,frames):
        total_array = [0.0] * 10
        array_results = [0.0] * 2
        array_player_counter = [0] * 10
        for i in range(1,len(players_hash_table)+1):
            #print("\n",players_hash_table[i])
            array_results = Mean_team_minuto.get_sprints_and_time_for_player(players_hash_table[i],frames)

            total_array = Mean_team_minuto.add_values(array_results[1], total_array)
            array_player_counter = Mean_team_minuto.count_players(array_results[0],array_player_counter)
        array_result = Mean_team_minuto.define_mean(total_array,array_player_counter)
        return array_result


    def select_high_intensity_team_values(players_hash_table,frames):
        total_array = [0.0] * 10
        array_results = [0.0] * 2
        array_player_counter = [0] * 10
        for i in range(1,len(players_hash_table)+1):
            #print("\n",players_hash_table[i])
            array_results = Mean_team_minuto.get_high_intensity_and_time_for_player(players_hash_table[i],frames)
            #print(array_alta_intensidad)
            total_array = Mean_team_minuto.add_values(array_results[1], total_array)
            array_player_counter = Mean_team_minuto.count_players(array_results[0],array_player_counter)

        array_result = Mean_team_minuto.define_mean(total_array,array_player_counter)
        return array_result
