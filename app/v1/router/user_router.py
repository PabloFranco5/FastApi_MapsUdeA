from fastapi import APIRouter
from fastapi import Depends
from fastapi import status
from fastapi import Body

from app.v1.schema.user_schema import *
from app.v1.service.user_service import *
from app.v1.model.user_model import *


from app.v1.utils.db import get_db


router = APIRouter(prefix="/api/v1")

@router.post(
    "/user/",
    tags = ["users"],
    response_model = UserBase,
    status_code=status.HTTP_201_CREATED,
    dependencies = [Depends(get_db)],
    summary = "Nueva Busqueda"
)
def create_user(user: UserBase = Body(...)):
    """
    ## Crearemos una nueva busqueda 

    ### Args
    la app va a recibir los siguientes parametros:
    - email: un correo valido
    - username: nombre de usuario
    - punto de partida: lugar donde nos econtramos 
    - punto de salida: lugar hacia donde queremos ir

    ### Returns
    - información solicitada de importancia:
    Usuario, punto de partida y punto de destino 
    """
    User = usuario(
        username = user.username,  
        punto_salida = user.punto_de_salida,
        punto_llegada = user.punto_de_llegada
        )


    User.save()

    return user
    


#A,b = create_user(user)
#print(b)
