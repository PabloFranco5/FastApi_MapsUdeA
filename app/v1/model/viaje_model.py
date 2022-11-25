from datetime import datetime
from peewee import ForeignKeyField
import peewee 

from app.v1.utils.db import db
from .user_model import *


class resumen_viaje(peewee.Model):
    Fecha_servicio = peewee.DateTimeField(default=datetime.now)
    Lugar_Salida = peewee.CharField(default=False)
    Lugar_Destino = peewee.CharField(default=False)
    Tiempo_trayecto = peewee.CharField(default=False)
    Distancia_recorrida = peewee.CharField(default=False)
    Clima = peewee.CharField(default=False)
    user = peewee.ForeignKeyField(usuario, backref="todos")

    class Meta:
        database = db

