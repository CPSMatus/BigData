"""_site2 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include

from django.conf import settings
from django.conf.urls.static import static


from _site2.views import analisis_jugador_jornada, analisis_torneo, table_jugadores,resumen_entrenamiento,dashboard_jugador,resumen_entrenamiento_filtros
from _site2.login.login_view import login_page
from _site2.torneo.torneo_view import resumen_jornadas
from _site2.ultima_jornada.ultima_jornada_view import resumen_ultima_jornada
from _site2.jugador_x_partido.jugador_x_partido_view  import jugador_x_partido

from django.views.generic import TemplateView
app_name = 'urls'




urlpatterns = [
    path('admin/', admin.site.urls),
    path('analisis_jugador_jornada/', analisis_jugador_jornada),
    path('login/', login_page),
    path('resumen_torneo/',analisis_torneo),

    path('table_jugadores/', table_jugadores),
    path('resumen_entrenamiento/', resumen_entrenamiento),
    path('dashboard_jugador/', dashboard_jugador),
    path('resumen_entrenamiento_filtros/', resumen_entrenamiento_filtros),

    #path('',include('frontend.urls')),
    path('resumen_jornadas/', resumen_jornadas),




    path('resumen_partido/', resumen_ultima_jornada),
    path('resumen_jugador/', jugador_x_partido,name='jugador_x_partido')
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
