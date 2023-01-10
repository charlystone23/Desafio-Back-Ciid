from fastapi import APIRouter, Response , Request
from starlette.status import HTTP_201_CREATED, HTTP_204_NO_CONTENT, HTTP_401_UNAUTHORIZED
from schema.user_schema import Userschema, DataUser
from config.db import engine
from model.users import users
from werkzeug.security import generate_password_hash , check_password_hash
from typing import List
from schema.provincias_schema import ProvinciaSchema
from model.provincias import provincias
from model.users import users
from middlewares.verify_token_route import verificarToken
from functions_jwt import validate_token


persona_prov = APIRouter()


@persona_prov.get("/")
def root():
    return {"message": "Im a fast api with a router"}

#personas
@persona_prov.get("/api/user", response_model=List[Userschema], tags=["User"]) 
def get_users():
    with engine.connect() as conn:
        result =conn.execute(users.select()).fetchall()
        return result

@persona_prov.get("/api/user/{user_id}", response_model=Userschema, tags=["User"])
def get_user(user_id: str,request:Request):
    a=verificarToken(request)
    if(a != None):
        return a
    with engine.connect() as conn:
        result= conn.execute(users.select().where(users.c.id == user_id)).first()
        return result

@persona_prov.post("/api/user", status_code=HTTP_201_CREATED, tags=["User"] )
def create_user(data_user: Userschema,request:Request):
    a=verificarToken(request)
    if(a != None):
        return a
    with engine.connect() as conn:  #con with nos aseguramso que la conbecion de la base de dadatos se cierre
        new_user = data_user.dict()
        conn.execute(users.insert().values(new_user))
        return Response(status_code=HTTP_201_CREATED)
    
""" @persona_prov.post("/api/user/login", status_code=200, tags=["User"])
def user_login(data_user : DataUser):
    with engine.connect() as conn:
        result = conn.execute(users.select().where(users.c.username == data_user.username)).first()
        if result != None:
            check_passw =check_password_hash( result[3],data_user.user_passw)
            if check_passw:
                return {"status": 200, "message": "accsess succes"}
        
        return {"status": HTTP_401_UNAUTHORIZED, "message": "accsess denied"} """




@persona_prov.put("/api/user/{user_id}", response_model=Userschema, tags=["User"])
def update_user(data_update: Userschema, user_id:str,request:Request):
    a=verificarToken(request)
    if(a != None):
        return a
    with engine.connect() as conn:
        
        conn.execute(users.update().values(lastname=data_update.lastname, name=data_update.name,dni=data_update.dni, fnac=data_update.fnac,adress=data_update.adress,id_Provincia=data_update.id_Provincia).where(users.c.id== user_id))
        
        result = conn.execute(users.select().where(users.c.id == user_id)).first()

        return result
    

@persona_prov.delete("/api/user/{user_id}", status_code=HTTP_204_NO_CONTENT, tags=["User"])
def delete_user(user_id: str,request:Request):
    a=verificarToken(request)
    if(a != None):
        return a
    with engine.connect() as conn:
        conn.execute(users.delete().where(users.c.id == user_id))
        return  Response(status_code=HTTP_204_NO_CONTENT)
    
#provincias

@persona_prov.get("/api/provincias",tags=["Provincias"])
def get_provincias():
    with engine.connect() as conn:
        result =conn.execute(provincias.select()).fetchall()
        return result


@persona_prov.get("/api/provincias/{prov_id}", tags=["Provincias"])
def get_single_province(prov_id: str,request:Request):
        a=verificarToken(request)
        if(a != None):
            return a
        with engine.connect() as conn:
            result= conn.execute(provincias.select().where(provincias.c.id == prov_id)).first()
            return result 
        
        
@persona_prov.post("/api/provincias", status_code=HTTP_201_CREATED, tags=["Provincias"])
def create_province(data_province: ProvinciaSchema,request:Request):
    a=verificarToken(request)
    if(a != None):
            return a
    with engine.connect() as conn:  #con with nos aseguramso que la conbecion de la base de dadatos se cierre
        #new_province = data_province.dict()
        new_province= {"name": data_province.name}
        conn.execute(provincias.insert().values(new_province))
        return Response(status_code=HTTP_201_CREATED)
    



@persona_prov.put("/api/provincias/{prov_id}" , tags=["Provincias"])
def update_provincia(data_update: ProvinciaSchema, prov_id: str,request:Request):
    a=verificarToken(request)
    if(a != None):
        return a
    with engine.connect() as conn:
        conn.execute(provincias.update().values(name=data_update.name).where(provincias.c.id== prov_id))
        
        result = conn.execute(provincias.select().where(users.c.id == prov_id)).first()

        return result
    
    
@persona_prov.delete("/api/provincias/{prov_id}", status_code=HTTP_204_NO_CONTENT, tags=["Provincias"])
def delete_user(prov_id: str,request:Request):    
    a=verificarToken(request)
    if(a != None):
        return a
    with engine.connect() as conn:
        conn.execute(users.delete().where(users.c.id_Provincia == prov_id))
        conn.execute(provincias.delete().where(provincias.c.id == prov_id))
        return  Response(status_code=HTTP_204_NO_CONTENT)