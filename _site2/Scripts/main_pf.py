from pf_diario import Pf_diario
import sys
from datetime import datetime

filename = str(sys.argv[1])
loc = ("/Users/smatus/Desktop/Club Puebla/Analisis Sesion/CL2022/")
#crear un objeto de la clase PF_diario con el nombre del archivo de Excel a leer
c = Pf_diario(filename,loc)

#Obtener un token de autenticacion para lograr postear a la base de datos
api_call_headers = c.obtain_token()

#Crear una nueva sesion de entrenamiento
#Fecha '2010/01/26:11:00:00AM'
fecha = '2021/12/28:12:00:00PM'
#CLAUSURA PRETEMPORADA
data_params = {
                'nombre_torneo':'CLAUSURA',
                'isRegular':0}


"""
now = datetime.now() # current date and time

from_calendar = now.strftime("%m-%d-%Y")


to_calendar =now.strftime("%m-%d-%Y")

print(from_calendar)
print(to_calendar)
"""

c.crear_jugador_sesion(api_call_headers)
wimu_sesion_data = c.crear_wimu_sesion_data(api_call_headers)
#c.get_last_session_info()

#print(data)







#Solo en caso de que el archivo recibido sea xls
#c.crear_wimu_sesion_data_xls(api_call_headers)


#No funciona desde codigo, debe ser en la base de datos
#c.crear_sesion_entrenamiento(api_call_headers,data_params,n_microciclo,sesion,lugar_entrenamiento,fecha)
