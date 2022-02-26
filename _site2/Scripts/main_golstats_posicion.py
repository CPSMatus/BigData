




loc_wimu = ("/Users/smatus/Desktop/Club Puebla/Excel Jornadas/CL2022/J6 CL 2022.xlsx")


loc_golstats_jugador = ("/Users/smatus/Desktop/Club Puebla/Excel Jornadas/CL2022/GOLSTATS CL2022/Matrix Puebla FC J6 CL 2022.xlsx")
loc_golstats_equipo = ("/Users/smatus/Desktop/Club Puebla/Excel Jornadas/CL2022/GOLSTATS CL2022/Matrix Liga MX J6 CL 2022.xlsx")


#Crear jugador x jornada
golstats_jugador = Golstats_jugador(loc_golstats_jugador,jornada_id)


jugador_jornada = Jugador_jornada(loc_golstats_jugador,loc_wimu)
jornada_id = 
#Obtener a todos los jugadores que participaron en la jornada
items = jugador_jornada.get_jugadores_jornada(jornada_id)

jugadores_array = golstats_jugador.post_golstats_posicion(items)
