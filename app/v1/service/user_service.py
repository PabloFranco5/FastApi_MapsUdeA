#PENDIENTE DE ELIMINAR 
from app.v1.model.user_model import usuario 
from app.v1.schema.user_schema import *



def create_User(user: UserBase):

    
    db_user = usuario(
        username = user.username,  
        punto_salida = user.punto_de_salida,
        punto_llegada = user.punto_de_llegada
        )


    db_user.save()

    return UserBase(
        username = db_user.username,
        punto_salida = db_user.punto_salida,
        punto_llegada = db_user.punto_llegada
    )



#def creacion_usuario(user: UserBase):
 #   usuario= user.create