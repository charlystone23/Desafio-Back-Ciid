from pydantic import BaseModel
from typing import Optional


class Userschema(BaseModel):
    id: Optional[str]
    name: str
    username: str
    user_passw: str
    id_Provincia: int
    
class DataUser(BaseModel):
    username:str
    user_passw: str