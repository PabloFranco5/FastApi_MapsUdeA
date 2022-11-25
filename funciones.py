import psycopg2
import requests 
import urllib
import datetime 
from datetime import date, datetime

conexion1 = psycopg2.connect(database="BaseDatos_MapsUdeA", user="postgres", password="1000895134j")
cur = conexion1.cursor()
cur.execute( "SELECT punto_salida,punto_llegada FROM usuario" )
query2= cur.fetchall()
conexion1.close()
print(query2[-1]) #ultimo dato del interfaz
origen = query2[-1][0]   #dato de salida del interfaz
destino = query2[-1][1]  #dato de llegada del interfaz
print(origen, destino)    


api_url = "http://www.mapquestapi.com/directions/v2/route?"
#el signo de interrogacion significa que vamos a separar la parte de la url con los recursos
key = "VUMTeSQl2G6JzINKnAuas25bl9dfkzAk"

def gps(origen, destino):
    url = api_url + urllib.parse.urlencode({"key":key, "from": origen, "to":destino}) 
    json_data = requests.get(url).json()
    duracion_del_viaje = json_data["route"]["formattedTime"]
    distancia = json_data["route"]["distance"] * 1.61
    nombre = ["Duración del viaje", "Distacia a Recorrer"]
    print("Indicaciones del trayecto")
    for each in json_data["route"]["legs"][0]["maneuvers"]:
        print(each["narrative"])

    return dict(zip(nombre, [duracion_del_viaje, distancia]))

if __name__ == "__main__":
    origen = origen
    destino = destino
    a = gps(origen, destino)
    print(a)

def clima(destino):
    urlclima_o = f"https://es.wttr.in/{destino}?format=j1"
    #urlclima_d = f"https://es.wttr.in/{destino}?format=j1"

    responseclima_o = requests.get(urlclima_o)
    #responseclima_d = requests.get(urlclima_d)
    clima_o = responseclima_o.json()
    #clima_d = responseclima_d.json()

    temperatura_origen = clima_o["current_condition"][0]["temp_C"]
    descripcion = clima_o["current_condition"][0]["lang_es"][0]["value"]
    return temperatura_origen, descripcion

def main(): 
    temperatura_destino, descripcion = clima(destino)
    print(f"La temperatura actual de {destino} es de {temperatura_destino} °C. {descripcion}")
    return f"La temperatura actual de {destino} es de {temperatura_destino} °C. {descripcion}"



if __name__ == "__main__":
    main()




conexion1 = psycopg2.connect(database="BaseDatos_MapsUdeA", user="postgres", password="1000895134j")
cursor1=conexion1.cursor()
#sql="insert into resumen_viaje(lugar_salida,lugar_destino,tiempo_trayecto,distancia_recorrida,clima) values (%s,%s,%s,%s,%s)"
p= main()
datos=( origen, destino, a["Duración del viaje"], a["Distacia a Recorrer"], p )
print(datos)
sql= f"insert into resumen_viaje({datos[0]},{datos[1]},{str(datos[2])},{str(datos[3])},{datos[4]})"
cursor1.execute(sql, datos)
conexion1.commit()
conexion1.close()