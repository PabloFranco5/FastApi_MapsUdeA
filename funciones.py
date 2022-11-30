import psycopg2
import requests 
import urllib
from app.v1.utils.settings import Settings

settings = Settings()

DB_NAME = settings.db_name
DB_USER = settings.db_user
DB_PASS = settings.db_pass
DB_HOST = settings.db_host
DB_PORT = settings.db_port

conexion = psycopg2.connect(database="BaseDatos_MapsUdeA", user="postgres", password="1000895134j")
cur = conexion.cursor()
cur.execute( "SELECT punto_salida,punto_llegada FROM usuario" )
query= cur.fetchall()
conexion.close()
print(query[-1]) #ultimo dato de lainterfaz
origen = query[-1][0]   #dato de salida de la interfaz
destino = query[-1][1]  #dato de llegada de la interfaz
print(origen, destino)    


api_url = "http://www.mapquestapi.com/directions/v2/route?"
key = "VUMTeSQl2G6JzINKnAuas25bl9dfkzAk"

def gps(origen, destino):
    """
    Función que se conecta con la api del clima
    devuelve un diccionario con la duración del viaje y la distación e
    imprime las instrucciones que se deben de seguir en automóvil para llegar al destino.
    """
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
    """
    Api que indica el clima de un lugar en específico.
    En este caso deseamos saber el clima que tiene el luegar de destino al que queremos llegar.
    """
    urlclima_o = f"https://es.wttr.in/{destino}?format=j1"
    #urlclima_d = f"https://es.wttr.in/{destino}?format=j1"

    responseclima_o = requests.get(urlclima_o)
    #responseclima_d = requests.get(urlclima_d)
    clima_o = responseclima_o.json()
    #clima_d = responseclima_d.json()

    temperatura_destino = clima_o["current_condition"][0]["temp_C"]
    descripcion = clima_o["current_condition"][0]["lang_es"][0]["value"]
    return temperatura_destino, descripcion

def main(): 
    temperatura_destino, descripcion = clima(destino)
    #print(f"La temperatura actual de {destino} es de {temperatura_destino} °C. {descripcion}")
    return f"La temperatura actual de {destino} es de {temperatura_destino} °C. {descripcion}"



if __name__ == "__main__":
    main()

#conexion1 = psycopg2.connect(database=DB_NAME, user=DB_USER, password= DB_PASS)
#cursor1=conexion1.cursor()
#p= main()
#datos=( origen, destino, a["Duración del viaje"], a["Distacia a Recorrer"], p )
#sql=f"""insert into resumen_viaje(lugar_salida,lugar_destino,tiempo_trayecto,distancia_recorrida,clima) 
#values ({datos[0]},{datos[1]},{datos[2]},{datos[3]},{datos[4]})"""
#cursor1.execute(sql, datos)
#conexion1.commit()
#conexion1.close()

#Pendiente que pablito pruebe esto a ver si funciona porque mi pc no sirve
conexion = psycopg2.connect(database=DB_NAME, user=DB_USER, password= DB_PASS)
cur = conexion.cursor()
p= main()
datos=(origen, destino, a["Duración del viaje"], a["Distacia a Recorrer"], p)
cur.execute( f"""insert into resumen_viaje(lugar_salida,lugar_destino,tiempo_trayecto,distancia_recorrida,clima) 
values ({datos[0]},{datos[1]},{datos[2]},{datos[3]},{datos[4]})""")
#query= cur.fetchall()
conexion.close()
