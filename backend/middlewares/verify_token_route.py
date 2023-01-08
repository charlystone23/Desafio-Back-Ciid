from fastapi import Request, Response
from functions_jwt import validate_token
from fastapi.routing import APIRoute
from starlette.status import HTTP_201_CREATED, HTTP_204_NO_CONTENT, HTTP_401_UNAUTHORIZED

def verificarToken(request:Request):
        auth= request.headers.get('Authorization')
        if auth != None:
            token= auth.split(" ")[1]
            validation_response =validate_token(token, output=False)    
            if validation_response != None:
                return Response(status_code=HTTP_401_UNAUTHORIZED,content="no authhh")
        else :
            return Response(status_code=HTTP_401_UNAUTHORIZED,content="no autoerizaDO") 
                    
            