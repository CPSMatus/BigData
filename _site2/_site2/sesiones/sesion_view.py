from django.shortcuts import render
from django.views.generic import CreateView
from django.http import JsonResponse


from _site2.sesiones.last_session import Ultima_sesion



def resumen_entrenamiento(request):

    c = Ultima_sesion()

    #si el metodo es post, esta llamada proviene del boton de filtrado
    if request.method =='POST':
        from_calendar = datetime.now()
        to_calendar = datetime.now()
        player = request.POST['players_select']
        #Obtener a los jugadores de la ultima sesion ! ! ! ! ! !! !! ! ! ! !! ! !! !
        from_calendar = request.POST['calendar_from']
        to_calendar = request.POST['calendar_to']
        posicion = request.POST['posicion_select']
        api_call_headers = c.obtain_token()

        # jugador - posicion
        if( (player != 0) and (posicion != 0)):
            print('calendar - jugador - posicion')
        # jugador -
        if( (player != 0) and (posicion == 0)):
            print('calendar - jugador - posicion')

        #        - posicion
        if( (player == 0) and (posicion != 0)):
            print('calendar - jugador - posicion')

        #        - posicion
        if( (player == 0) and (posicion != 0)):
            print('calendar - jugador - posicion')




        print(player)
        print(from_calendar)
        print(to_calendar)
        print(posicion)

#Si el metodo es get, se da lectura, es decir se requieren los datos de la ultima sesion
    #if request.method =='GET':
    api_call_headers = c.obtain_token()
    table_list = c.get_last_session_wimu_info(api_call_headers)
    context={'table_list' : table_list['items']}

    return render(request,'resumen_entrenamiento_table2.html',context)
