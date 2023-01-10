from fastapi import APIRouter, Header
from pydantic import BaseModel
from functions_jwt import write_token,validate_token
from fastapi.responses import JSONResponse

auth_routes= APIRouter()

class User(BaseModel):
    usernam:str
    passwor:str

@auth_routes.post("/login" , tags=["Auth"])
def login(user: User):
    print(user.dict())
    if user.usernam == "admin":
        if user.passwor=="admin":
            return write_token(user.dict()) 
        else:
            return JSONResponse(content={"message":"Credenciales invalidaS"},status_code=404)    
    else:
        return JSONResponse(content={"message":"Credenciales invalidaS"},status_code=404)
    
@auth_routes.post("/verify/token", tags=["Auth"])
def verify_token(Authorization: str= Header(None)):
    token = Authorization.split(" ")[1]
    return validate_token(token,output=True)

