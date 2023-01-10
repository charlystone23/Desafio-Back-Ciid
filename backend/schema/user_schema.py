from pydantic import BaseModel
from typing import Optional


class Userschema(BaseModel):
    id: Optional[str]
    lastname: str
    name: str
    dni: str
    fnac: str
    adress: str
    id_Provincia: int
    
class DataUser(BaseModel):
    username:str
    user_passw: str