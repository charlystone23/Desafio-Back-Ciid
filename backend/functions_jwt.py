from jwt import encode , decode
from jwt import exceptions
from datetime import datetime, timedelta
from os import getenv
from fastapi.responses import JSONResponse

def expiredate(days:int):
    date = datetime.now()
    new_date= date +timedelta(days)
    return new_date

""" informacion a encriptar """
def write_token(data: dict):
    token=encode(payload={**data,"exp":expiredate(2) },key=getenv("SECRET"), algorithm="HS256")
    return token 


def validate_token(token, output=False):
    try:
        if output:
            return decode(token, key=getenv("SECRET"),algorithms=["HS256"] )
        decode(token, key=getenv("SECRET"),algorithms=["HS256"] )
    except exceptions.DecodeError:
        return JSONResponse(content={"message": "Invalid Token"}, status_code=401)
    except exceptions.ExpiredSignatureError:
        return JSONResponse(content={"message": "Token Expired"}, status_code=401)
    
    