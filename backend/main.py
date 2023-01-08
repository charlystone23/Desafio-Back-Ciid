from fastapi import FastAPI
from router.router import persona_prov
from fastapi.middleware.cors import CORSMiddleware
from dotenv import load_dotenv
from router.auth import auth_routes
""" instancia """

app= FastAPI()


app.include_router(auth_routes,prefix="/api")
""" cargar las variables de entorno """
load_dotenv()


origins = ["*"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)   

app.include_router(persona_prov)
