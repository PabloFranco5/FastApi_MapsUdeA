#from fastapi import HTTPException, status


from app.v1.model.user_model import usuario 
from app.v1.schema.user_schema import UserBase, User



def create_user(user: UserBase):

    #get_user = usuario.filter((usuario.email == UserBase.email) | (usuario.username_id == UserBase.username)).first()
    #if get_user:
     #   msg = "Este Email ya se encuentra registrado"
      #  if get_user.username == user.username:
       #     msg = "Username en uso"
        #raise HTTPException(
         #   status_code=status.HTTP_400_BAD_REQUEST,
          #  detail=msg
        #)

    db_user = usuario(
        username = user.username, 
        email = user.email, 
        telefono = user.numero_telefono,
        punto_salida = user.punto_de_salida,
        punto_llegada = user.punto_de_llegada
        )
    db_user.save()

    return User(
        id = db_user.id,
        username = db_user.username_id,
        email = db_user.email,
        telefono = db_user.telefono,
        punto_salida = db_user.punto_salida,
        punto_llegada = db_user.punto_llegada
    )

