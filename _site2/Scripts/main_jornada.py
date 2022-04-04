from golstats_equipo import Golstats_equipo
from golstats_jugador import Golstats_jugador
from datetime import datetime
from jugador_jornada import Jugador_jornada
import sys
# adding Folder_2 to the system path
sys.path.insert(0, '/Users/smatus/Documents/Python by example/project 1/_site2/_site2/ultima_jornada')
from get_ultima_jornada import Ultima_Jornada
from jornada_dataframe import Jornada

loc_wimu = ("/Users/smatus/Desktop/Club Puebla/Excel Jornadas/CL2022/J11 CL 2022.xlsx")



loc_golstats_jugador = ("/Users/smatus/Desktop/Club Puebla/Excel Jornadas/CL2022/GOLSTATS CL2022/Matrix Puebla FC J11 CL 2022.xlsx")
loc_golstats_equipo = ("/Users/smatus/Desktop/Club Puebla/Excel Jornadas/CL2022/GOLSTATS CL2022/Matrix Liga MX J11 CL 2022.xlsx")



#Instanciar clases
#Leer los archivos para asegurarse que son correctos
jornada_wimu = Jornada(loc_wimu)

golstats_jugador = Golstats_jugador(loc_golstats_jugador,jornada_id)

#Crear estadisiticas de golstats x Equipo
golstats_equipo = Golstats_equipo(loc_golstats_equipo)


#Obtener un token de autenticacion para lograr postear a la base de datos
api_call_headers = golstats_equipo.create_token()
ultima_jornada = Ultima_Jornada()

#jornada_id = ultima_jornada.get_jornada_id()
jornada_info = ultima_jornada.get_jornada_info()
jornada_id =  jornada_info['jornada_id']


print("JORNADA ID: \n", jornada_id)



#Post a tu equipo
print("Selecciona el header de tu equipo:")
tu_equipo_header = golstats_equipo.select_headers()
puebla_id = 18 #Puebla ID in database
golstats_equipo.create_ofensiva(tu_equipo_header,jornada_id,puebla_id)
golstats_equipo.create_defensiva(tu_equipo_header,jornada_id,puebla_id)
golstats_equipo.create_general(tu_equipo_header,jornada_id)


#Post al rival
print("Selecciona del equipo rival: ")
rival_header = golstats_equipo.select_headers()
golstats_equipo.create_ofensiva(rival_header,jornada_id,jornada_info['id_rival'])
golstats_equipo.create_defensiva(rival_header,jornada_id,jornada_info['id_rival'])

#Crear jugador x jornada

golstats_jugador.crear_jugador_jornada()

#Estadisticas de WIMU X JORNADA

jugador_jornada = Jugador_jornada(loc_golstats_jugador,loc_wimu)

#Post jugador x jornada
items = jugador_jornada.get_jugadores_jornada(jornada_id)
jugadores_array = golstats_jugador.post_golstats_posicion(items)


players = jornada_wimu.fill_players()
print(players)
#Extraer las columnas del excel para analizar solo el dataframe
result = jornada_wimu.create_df()

#Obtener los lapsos a examinar, eliminar drills y primer tiempo
frames = jornada_wimu.create_df_parameters(result)


jugador_jornada.post_wimu_values(players,frames,items)
