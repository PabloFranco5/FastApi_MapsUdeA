from fastapi import APIRouter
from fastapi import Depends
from fastapi import status
from fastapi import Body

from app.v1.schema.user_schema import *
from app.v1.service.user_service import *

from app.v1.utils.db import get_db


router = APIRouter(prefix="/api/v1")

@router.post(
    "/user/",
    tags = ["users"],
    status_code = status.HTTP_201_CREATED,
    response_model = User,
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
    - telefono: numero de contacto 
    - punto de partida: lugar donde nos econtramos 
    - punto de salida: lugar hacia donde queremos ir

    ### Returns
    - información solicitada 
    """
    return create_user(user)
    