from django.shortcuts import render
from django.views.generic import CreateView
from django.http import JsonResponse

def table_jugadores(request):

    data = endpoint_torneo.get_jugadores()


    context={'jugadores' : data['items']}
    #print(context)
    return render(request,'table_jugadores.html',context)
