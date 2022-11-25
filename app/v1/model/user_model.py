import peewee

from app.v1.utils.db import db

class usuario(peewee.Model):
#    email = peewee.CharField(unique=True, index=True)
    username = peewee.CharField(unique=True, index=True)
    punto_salida = peewee.CharField(unique=False, index=True)
    punto_llegada = peewee.CharField(unique=False, index=True)

    class Meta:
        database = db