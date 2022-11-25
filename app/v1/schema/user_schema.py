from pydantic import BaseModel
from pydantic import Field
#from pydantic import EmailStr


class UserBase(BaseModel):
    username: str 
    punto_de_salida: str 
    punto_de_llegada: str 


