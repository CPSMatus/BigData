from django.shortcuts import render,redirect

from _site2.ultima_jornada.get_ultima_jornada import Ultima_Jornada


def resumen_ultima_jornada(request):

    ultima_jornada = Ultima_Jornada()

    ultima_jornada_info = ultima_jornada.get_jornada_wimu_info()

    jugadores_info = ultima_jornada.get_table()

    #Se puede obtener ultima jornada info de manera independiente

    ultima_jornada_info = ultima_jornada.get_jornada_info()
    #echa_y_hora = ultima_jornada.get_fecha_y_hora(ultima_jornada_info['fecha'])

    context = {
        'jugadores' : jugadores_info ,
        'ultima_jornada': ultima_jornada_info,
        }

    return render(request,'resumen_partido_table.html',context)
