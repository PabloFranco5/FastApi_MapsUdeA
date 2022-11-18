
from peewee import SqliteDatabase, CharField, DateField, ForeignKeyField, Model, DateTimeField, PostgresqlDatabase
#db = PostgresqlDatabase("Maps_Udea", user="postgres", password="1000895134j", host="localhost", port=5432)
db = SqliteDatabase('academia.db')

class usuario(Model):
    email = CharField()
    username_id = CharField()
    telefono = CharField()


    class Meta:
        database = db

class resumen_viaje(Model):
    Fecha_servicio = DateTimeField()
    Lugar_Salida = CharField(default=False)
    Lugar_Destino = CharField(default=False)
    Tiempo_trayecto = DateField(default=False)
    Distancia_recorrida = DateTimeField(default=False)
    Clima = CharField(default=False)
    username_id = CharField()
    
    class Meta:
        database = db

db.connect()
db.create_tables([usuario, resumen_viaje])