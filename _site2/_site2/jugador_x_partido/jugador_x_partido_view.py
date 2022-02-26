from django.shortcuts import render
from django.views.generic import CreateView
from django.http import JsonResponse
from _site2.ultima_jornada.get_ultima_jornada import Ultima_Jornada
from _site2.jugador_x_partido.jugador_x_partido import Jugador_x_partido_handler
from _site2.ajax_handler.ajax_handler import Ajax_handler


template_name = "resumen_jugador_xpartido.html"



def jugador_x_partido(request):

    if request.method =='POST':
        #Obtener de un form el id del jugador por partido

        id_jugador = request.POST.get("jugador_jornada_id")
        id_jornada = request.POST.get("jornada_id")
        print("ID JUGADOR: ", id_jugador)
        print("ID_JORNADA: ", id_jornada )

        context={ 'jugador' : id_jugador,
                'jornada_id': id_jornada }

    return render(request,template_name,context)


"""
    def render_to_response(self, context, **response_kwargs):
            """  """
            if self.request.is_ajax():
                print('Es un peticon ajax*********')
                return JsonResponse(context)
            else:
                response_kwargs.setdefault('content_type', self.content_type)
                return self.response_class(
                    request=self.request,
                    template=self.get_template_names(),
                    context=context,
                    using=self.template_engine,
                    **response_kwargs
                )
"""
