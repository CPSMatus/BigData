import pandas as pd
import numpy as np
import openpyxl
import numpy as np
import matplotlib.pyplot as plt
# Program extracting first column

import seaborn as sns

import xlrd



class Jornada2:


    start_cell = 0

    selected_player = ""

    distance_array = []
    sprint_abs_cnt_array = []

    string_game = ""


    def set_string_game(game):
        global string_game
        string_game = game


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

    def send_parameters():
        #for para detectar las celdas
        global loc
        global start_cell

        global wb
        global distance_sheet
        global hse_sheet
        global start_first_time_row
        global start_second_time_row
        global start_first_time_count
        global start_second_time_count
        loc = ("/Users/smatus/Desktop/Club Puebla/Excel Jornadas/")

        loc = loc + string_game

        wb = xlrd.open_workbook(loc)
        distance_sheet = wb.sheet_by_index(0)
        hse_sheet = wb.sheet_by_index(3)

        distance_sheet.cell_value(0, 0)

        for i in range(0,distance_sheet.nrows):

            #termina seleccion de los jugadores
            if distance_sheet.cell_value(i, 0) == "Drills":
                start_cell = i + 1

            #termina seleccion de los jugadores
            if distance_sheet.cell_value(i, 0) == "PRIMER TIEMPO" :
                start_first_time_row = i + 1

            #termina seleccion de los jugadores
            if distance_sheet.cell_value(i, 0) == "SEGUNDO TIEMPO":
                start_second_time_row = i + 1


            #termina seleccion de los jugadores
            if distance_sheet.cell_value(i, 0) == "0  10" :
                start_first_time_count = i + 1


            #termina seleccion de los jugadores
            if distance_sheet.cell_value(i, 0) == "0  5" :
                start_second_time_count = i + 1


        #print("\n Starting at cell : " ,start_cell )

        #print("\n First time row starts at : " ,start_first_time_row )

        #print("\n Second time row starts at : " ,start_second_time_row )


        #print("\n First time count starts at : " ,start_first_time_count )

        #print("\n Second time count starts at : " ,start_second_time_count )

    def fill_players():
        global n_players
        global players_hash_table

        players_hash_table = {}
        n_players = 0
        #cuantos jugaron todo el partido
        for i in range(start_cell,distance_sheet.nrows):
            #termina seleccion de los jugadores
            if distance_sheet.cell_value(i, 0) == "":
                break
            n_players = n_players + 1
            print(n_players , distance_sheet.cell_value(i, 0))
            players_hash_table[n_players] = distance_sheet.cell_value(i, 0)
        print("JUGARON EN TOTAL: ",n_players)
        return players_hash_table

    def select_player():
        global selected_player

        #print("\n N. JUGADORES: (del partido)" ,n_players )
        Jornada.fill_players()

        #print ("\n Select the number of the player to analyze")
        player_int = int(input())
        selected_player = players_hash_table[player_int]

        #print("\n Selected player: ", selected_player)
        return selected_player

    def select_distance_values(selected_player):
        distance_array = []
        #almacenar  el restante del
        distance_45_to_50 = 0

        distance = 0
        found = False

        distance_cell_number = 4
        array_count = 0
        reading = ""

        #Select the values distance (m) for first time
        for i in range(start_first_time_count,start_second_time_row):
            reading = distance_sheet.cell_value(i, 0)
            if reading == selected_player:
                distance  = distance_sheet.cell_value(i, distance_cell_number)
                found = True

            if reading == "":
                array_count = array_count + 1
                if found == True:
                    found = False
                    if (array_count < 5):
                        #print("First time, Adding: ", distance , " position :" , i, " count: " , array_count)
                        distance_array = np.append(distance_array,distance)
                        distance = 0
                    else:
                        #print(" Distance Adding to distance_45_to_50 ", distance)
                        distance_45_to_50 += distance

                else:
                    if (array_count < 5):
                        #print("Second time, Adding: ", 0 , " position :" , i)
                        distance_array = np.append(distance_array,0)


        #print("Adding Distance Primer TIEMPO from 45 to 50: ",distance_45_to_50, " count: " , array_count)
        distance_array = np.append(distance_array,distance_45_to_50)
        array_count = array_count + 1
        #re start the value for the second time
        counter = 0
        distance_45_to_50 = 0
        reading = ""
        sum = 0
        found = False
        laps = 0
        #Select the values distance (m) for second time
        for i in range(start_second_time_count,distance_sheet.nrows):

            reading = distance_sheet.cell_value(i, 0)
            if reading == selected_player:
                distance  = distance_sheet.cell_value(i, distance_cell_number)
                found = True

            if reading == "":
                laps = laps + 1
                if found == True:
                    found = False
                    if (array_count < 10):
                        if (laps == 1):
                            distance_array = np.append(distance_array,distance)
                        #    print("Second time, Adding: ", distance , " position :" , i, " count: " , array_count)
                            array_count = array_count + 1
                        elif (laps%2 == 1):
                            sum += distance
                            distance_array = np.append(distance_array,sum)
                        #    print("Second time, Adding: ", sum , " position :" , i, " count: " , array_count)
                            array_count = array_count + 1

                            sum = 0
                        else:
                            sum += distance
                        distance = 0
                    else:
                        #print("Distance Second time Adding to distance_45_to_50 ", distance)
                        distance_45_to_50 += distance
                else:
                    if (array_count < 10):
                        if (laps == 1):
                            #no se encontro, es el primer lapso del segundo tiempo 45 - 50
                            distance_array = np.append(distance_array,0)
                            array_count = array_count + 1
                        elif (laps%2 == 1):
                            sum += distance
                            distance_array = np.append(distance_array,sum)
                            array_count = array_count + 1
                           #print("Second time, Adding: ", sum, " position :" , i )
                            sum = 0
                            distance = 0
                        else:
                            sum += 0
                    else:
                        distance_45_to_50 += 0


        #print("Adding Distance SEGUNDO tiempo from 45 to 50: ",distance_45_to_50, " count: " , array_count)
        distance_array = np.append(distance_array,distance_45_to_50)


        return distance_array

    def select_high_intensity_distance(selected_player):
        high_intensity_distance_array = []

        #almacenar en un arreglo el restante del
        distance_45_to_50 = 0

        distance_18_21 = 0
        distance_21_24 = 0
        distance_24_50 = 0
        total = 0
        found = False

        distance_18_21_cell_number = 16
        distance_21_24_cell_number = 17
        distance_24_50_cell_number = 18

        array_count = 0
        reading = ""

        #Select the values distance (m) for first time
        for i in range(start_first_time_count,start_second_time_row):
            reading = distance_sheet.cell_value(i, 0)
            if reading == selected_player:
                distance_18_21  = distance_sheet.cell_value(i, distance_18_21_cell_number)
                distance_21_24  = distance_sheet.cell_value(i, distance_21_24_cell_number)
                distance_24_50  = distance_sheet.cell_value(i, distance_24_50_cell_number)
                total = distance_18_21 + distance_21_24 + distance_24_50
                found = True

            if reading == "":
                array_count = array_count + 1
                if found == True:
                    found = False
                    if (array_count < 5):
                    #    print("First time, Adding: ", total , " position :" , i, " count: " , array_count)
                        high_intensity_distance_array = np.append(high_intensity_distance_array,total)
                        total = 0
                    else:
                    #    print(" Distance Adding to distance_45_to_50 ", total)
                        distance_45_to_50 += total

                else:
                    if (array_count < 5):
                #    print("Second time, Adding: ", 0 , " position :" , i)
                        high_intensity_distance_array = np.append(high_intensity_distance_array,0)


        #print("Adding Distance Primer TIEMPO from 45 to 50: ",distance_45_to_50, " count: " , array_count)
        high_intensity_distance_array = np.append(high_intensity_distance_array,distance_45_to_50)
        array_count = array_count + 1
        #re start the value for the second time
        counter = 0
        distance_45_to_50 = 0
        reading = ""
        sum = 0
        found = False
        laps = 0
        #Select the values total (m) for second time
        for i in range(start_second_time_count,distance_sheet.nrows):

            reading = distance_sheet.cell_value(i, 0)
            if reading == selected_player:
                distance_18_21  = distance_sheet.cell_value(i, distance_18_21_cell_number)
                distance_21_24  = distance_sheet.cell_value(i, distance_21_24_cell_number)
                distance_24_50  = distance_sheet.cell_value(i, distance_24_50_cell_number)
                total = distance_18_21 + distance_21_24 + distance_24_50
                found = True

            if reading == "":
                laps = laps + 1
                if found == True:
                    found = False
                    if (array_count < 10):
                        if (laps == 1):
                            high_intensity_distance_array = np.append(high_intensity_distance_array,total)
                        #    print("Second time, Adding: ", total , " position :" , i, " count: " , array_count)
                            array_count = array_count + 1
                        elif (laps%2 == 1):
                            sum += total
                            high_intensity_distance_array = np.append(high_intensity_distance_array,sum)
                        #    print("Second time, Adding: ", sum , " position :" , i, " count: " , array_count)
                            array_count = array_count + 1

                            sum = 0
                        else:
                            sum += total
                        total = 0
                    else:
                        #print("total Second time Adding to distance_45_to_50 ", total)
                        distance_45_to_50 += total
                else:
                    if (array_count < 10):
                        if (laps == 1):
                            #no se encontro, es el primer lapso del segundo tiempo 45 - 50
                            high_intensity_distance_array = np.append(high_intensity_distance_array,0)
                            array_count = array_count + 1
                        elif (laps%2 == 1):
                            sum += total
                            high_intensity_distance_array = np.append(high_intensity_distance_array,sum)
                            array_count = array_count + 1
                           #print("Second time, Adding: ", sum, " position :" , i )
                            sum = 0
                            total = 0
                        else:
                            sum += 0
                    else:
                        distance_45_to_50 += 0


        #print("Adding Distance SEGUNDO tiempo from 45 to 50: ",distance_45_to_50, " count: " , array_count)
        high_intensity_distance_array = np.append(high_intensity_distance_array,distance_45_to_50)


        return high_intensity_distance_array

    def select_sprint_abs_cnt(selected_player):

        sprint_abs_cnt_cell_number = 3
        for i in range(0,hse_sheet.nrows):

            #termina seleccion de los jugadores
            if hse_sheet.cell_value(i, 0) == "Drills":
                start_cell = i + 1
                #print("\n Starting at cell : " ,start_cell )

            #termina seleccion de los jugadores
            if hse_sheet.cell_value(i, 0) == "PRIMER TIEMPO" :
                start_first_time_row = i + 1
                #print("\n First time row starts at : " ,start_first_time_row )

            #termina seleccion de los jugadores
            if hse_sheet.cell_value(i, 0) == "SEGUNDO TIEMPO":
                start_second_time_row = i + 1
                #print("\n Second time row starts at : " ,start_second_time_row )

            #termina seleccion de los jugadores
            if hse_sheet.cell_value(i, 0) == "0  10" :
                start_first_time_count = i + 1
                #print("\n First time count starts at : " ,start_first_time_count )

            #termina seleccion de los jugadores
            if hse_sheet.cell_value(i, 0) == "0  5" :
                start_second_time_count = i + 1
                #print("\n Second time count starts at : " ,start_second_time_count )


        sprints_array = []
        #almacenar en un arreglo el restante del
        sprints_45_to_50 = 0
        sprints = 0
        reading = ""
        found = False

        array_count = 0
        reading = ""

        #Select the values distance (m) for first time
        for i in range(start_first_time_count,start_second_time_row):
            reading = hse_sheet.cell_value(i, 0)
            if reading == selected_player:
                sprints  = hse_sheet.cell_value(i, sprint_abs_cnt_cell_number)
                found = True

            if reading == "":
                array_count = array_count + 1
                if found == True:
                    found = False
                    if (array_count < 5):
                        #print("First time, Adding: ", sprints , " position :" , i, " count: " , array_count)
                        sprints_array = np.append(sprints_array,sprints)
                        sprints = 0
                    else:
                    #    print(" Distance Adding to sprints_45_to_50 ", sprints)
                        sprints_45_to_50 += sprints

                else:
                    if (array_count < 5):
                        #print("Second time, Adding: ", 0 , " position :" , i)
                        sprints_array = np.append(sprints_array,0)


        #print("Adding Distance Primer TIEMPO from 45 to 50: ",sprints_45_to_50, " count: " , array_count)
        sprints_array = np.append(sprints_array,sprints_45_to_50)
        array_count = array_count + 1
        #re start the value for the second time
        counter = 0
        sprints_45_to_50 = 0
        reading = ""
        sum = 0
        found = False
        laps = 0
        #Select the values distance (m) for second time
        for i in range(start_second_time_count,hse_sheet.nrows):

            reading = hse_sheet.cell_value(i, 0)
            if reading == selected_player:
                sprints  = hse_sheet.cell_value(i, sprint_abs_cnt_cell_number)
                found = True

            if reading == "":
                laps = laps + 1
                if found == True:
                    found = False
                    if (array_count < 10):
                        if (laps == 1):
                            sprints_array = np.append(sprints_array,sprints)
                        #    print("Second time, Adding: ", sprints , " position :" , i, " count: " , array_count)
                            array_count = array_count + 1
                        elif (laps%2 == 1):
                            sum += sprints
                            sprints_array = np.append(sprints_array,sum)
                        #    print("Second time, Adding: ", sum , " position :" , i, " count: " , array_count)
                            array_count = array_count + 1

                            sum = 0
                        else:
                            sum += sprints
                        sprints = 0
                    else:
                        #print("sprints Second time Adding to sprints_45_to_50 ", sprints)
                        sprints_45_to_50 += sprints
                else:
                    if (array_count < 10):
                        if (laps == 1):
                            #no se encontro, es el primer lapso del segundo tiempo 45 - 50
                            sprints_array = np.append(sprints_array,0)
                            array_count = array_count + 1
                        elif (laps%2 == 1):
                            sum += sprints
                            sprints_array = np.append(sprints_array,sum)
                            array_count = array_count + 1
                           #print("Second time, Adding: ", sum, " position :" , i )
                            sum = 0
                            sprints = 0
                        else:
                            sum += 0
                    else:
                        sprints_45_to_50 += 0


        #print("Adding Distance SEGUNDO tiempo from 45 to 50: ",sprints_45_to_50, " count: " , array_count)
        sprints_array = np.append(sprints_array,sprints_45_to_50)


        return sprints_array

    def define_time_values():
        time_array = []
        duration_cell_number = 2
        time_45_to_50 = 0
        duration = 0

        #Select the values distance (m) for first time
        for i in range(start_first_time_count,start_second_time_row):
            #we assume that the first time is th biggest time
            reading = distance_sheet.cell_value(i, duration_cell_number)
            array_count = array_count + 1
            if (array_count < 5):
                if (duration < reading):
                    distance_array = np.append(distance_array,distance)
                    distance = 0
                else:
                    #print(" Distance Adding to distance_45_to_50 ", distance)
                    distance_45_to_50 += distance

            else:
                if (array_count < 5):
                    #print("Second time, Adding: ", 0 , " position :" , i)
                    distance_array = np.append(distance_array,0)


        #print("Adding Distance Primer TIEMPO from 45 to 50: ",distance_45_to_50, " count: " , array_count)
        distance_array = np.append(distance_array,distance_45_to_50)
        array_count = array_count + 1


    ## __TO DEFINE __ ##
    def select_player_time_values():
        #Obtener la duracion de cada uno de los jugadores, para dividir unicamente
        #entre aquellos que jugaron mas del 75% del analisis
        distance_array = []
        #almacenar  el restante del
        distance_45_to_50 = 0

        distance = 0
        found = False

        distance_cell_number = 2
        array_count = 0
        reading = ""

        #Select the values distance (m) for first time
        for i in range(start_first_time_count,start_second_time_row):
            reading = distance_sheet.cell_value(i, 0)
            if reading == selected_player:
                distance  = distance_sheet.cell_value(i, distance_cell_number)
                found = True

            if reading == "":
                array_count = array_count + 1
                if found == True:
                    found = False
                    if (array_count < 5):
                        #print("First time, Adding: ", distance , " position :" , i, " count: " , array_count)
                        distance_array = np.append(distance_array,distance)
                        distance = 0
                    else:
                        #print(" Distance Adding to distance_45_to_50 ", distance)
                        distance_45_to_50 += distance

                else:
                    if (array_count < 5):
                        #print("Second time, Adding: ", 0 , " position :" , i)
                        distance_array = np.append(distance_array,0)


        #print("Adding Distance Primer TIEMPO from 45 to 50: ",distance_45_to_50, " count: " , array_count)
        distance_array = np.append(distance_array,distance_45_to_50)
        array_count = array_count + 1
        #re start the value for the second time
        counter = 0
        distance_45_to_50 = 0
        reading = ""
        sum = 0
        found = False
        laps = 0
        #Select the values distance (m) for second time
        for i in range(start_second_time_count,distance_sheet.nrows):

            reading = distance_sheet.cell_value(i, 0)
            if reading == selected_player:
                distance  = distance_sheet.cell_value(i, distance_cell_number)
                found = True

            if reading == "":
                laps = laps + 1
                if found == True:
                    found = False
                    if (array_count < 10):
                        if (laps == 1):
                            distance_array = np.append(distance_array,distance)
                        #    print("Second time, Adding: ", distance , " position :" , i, " count: " , array_count)
                            array_count = array_count + 1
                        elif (laps%2 == 1):
                            sum += distance
                            distance_array = np.append(distance_array,sum)
                        #    print("Second time, Adding: ", sum , " position :" , i, " count: " , array_count)
                            array_count = array_count + 1

                            sum = 0
                        else:
                            sum += distance
                        distance = 0
                    else:
                        #print("Distance Second time Adding to distance_45_to_50 ", distance)
                        distance_45_to_50 += distance
                else:
                    if (array_count < 10):
                        if (laps == 1):
                            #no se encontro, es el primer lapso del segundo tiempo 45 - 50
                            distance_array = np.append(distance_array,0)
                            array_count = array_count + 1
                        elif (laps%2 == 1):
                            sum += distance
                            distance_array = np.append(distance_array,sum)
                            array_count = array_count + 1
                           #print("Second time, Adding: ", sum, " position :" , i )
                            sum = 0
                            distance = 0
                        else:
                            sum += 0
                    else:
                        distance_45_to_50 += 0


        #print("Adding Distance SEGUNDO tiempo from 45 to 50: ",distance_45_to_50, " count: " , array_count)
        distance_array = np.append(distance_array,distance_45_to_50)


        return distance_array





"""
    def find_second_time_duration(start_second_time_row,start_second_time_count):
        #assume the first cell is the bigger cell
        second_time_duration_string =  distance_sheet.cell_value(start_second_time_row + 1
         ,duration_cell_number)

         #if the read value is greater , replace first_time_duration_string
        for i in range(start_second_time_row,start_second_time_count):
            if distance_sheet.cell_value(i,duration_cell_number) > second_time_duration_string:
                second_time_duration_string = distance_sheet.cell_value(i,duration_cell_number)

        second_time_duration_array = second_time_duration_string.split(":")
        second_time_minutes_int = int(second_time_duration_array[1])
        return second_time_minutes_int

    def find_first_time_duration(start_first_time_row,start_first_time_count):
        #assume the first cell is the bigger cell
        first_time_duration_string =  distance_sheet.cell_value(start_first_time_row + 1
         ,duration_cell_number)

         #if the read value is greater , replace first_time_duration_string
        for i in range(start_first_time_row,start_first_time_count):
            if distance_sheet.cell_value(i,duration_cell_number) > first_time_duration_string:
                first_time_duration_string = distance_sheet.cell_value(i,duration_cell_number)

        first_time_duration_array = first_time_duration_string.split(":")
        first_time_minutes_int = int(first_time_duration_array[1])
        return first_time_minutes_int
"""

"""

    distance_array = select_distance_values(selected_player,start_first_time_count,start_second_time_row,start_second_time_count,players_hash_table[n_players-1])

    high_intensity_distance_array = select_high_intensity_distance(selected_player,start_first_time_count,start_second_time_row,start_second_time_count)

    sprint_abs_cnt_array = select_sprint_abs_cnt(selected_player)


    #print ("\n Distance array: ",distance_array)


    #print ("\n High Intensity Distance array: ",high_intensity_distance_array)


    #print ("\n High Intensity Distance array: ",sprint_abs_cnt_array)


    minutes_interval = send_minutes_interval()
    print(minutes_interval)



    #Construction pandas dataframe
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
    axis[0,0].set_title("Distance (m)")
    axis[0,0].grid()

    axis[0,1].plot(distance_high_intensity['Minutes'], distance_high_intensity['Distance'])
    axis[0,1].set_title("Distancia Alta Intensidad(m)")
    axis[0,1].grid()

    axis[1,0].plot(sprint_abs_cnt['Minutes'], sprint_abs_cnt['Sprints'])
    axis[1,0].set_title("Sprints")
    axis[1,0].grid()


    plt.show()
"""
