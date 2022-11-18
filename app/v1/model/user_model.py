import peewee

from app.v1.utils.db import db

class usuario(peewee.Model):
    email = peewee.CharField(unique=True, index=True)
    username_id = peewee.CharField(unique=True, index=True)
    telefono = peewee.CharField()
    punto_salida = peewee.CharField()
    punto_llegada = peewee.CharField()

    class Meta:
        database = db