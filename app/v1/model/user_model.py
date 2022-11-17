import peewee

from app.v1.utils.db import db

class usuario(peewee.Model):
    email = peewee.CharField(unique=True, index=True)
    username = peewee.CharField(unique=True, index=True)
    lugar_salida = peewee.CharField()
    lugar_llegada = peewee.CharField()

    class Meta:
        database = db