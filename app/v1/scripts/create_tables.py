from app.v1.model.user_model import usuario
from app.v1.model.viaje_model import resumen_viaje

from app.v1.utils.db import db

def create_tables():
    """
    Creación de las tablas donde se almacena la información relevante
    en donde se resume el viaje y el clima
    """
    with db:
        db.create_tables([usuario, resumen_viaje])
        