from django.shortcuts import render,redirect
from resumen_torneo import Resumen_torneo

endpoint_torneo = Resumen_torneo()

def resumen_jornadas(request):
    #Obtener todos los torneos
    #Obtener el ultimo torneo
    #Obtener a todos los Jugadores
    #Obtener todas las jornadas
    jornadas = endpoint_torneo.get_jornadas()
    jugadores = endpoint_torneo.get_jugadores()
    jugador_jornada = endpoint_torneo.get_jugadores_jornada()
    context = {
        'jornadas' : jornadas['items'],
        'jugadores' : jugadores['items'],
        'jugador_jornada':jugador_jornada['items']
        }

    return render(request,'resumen_partido.html',context)
