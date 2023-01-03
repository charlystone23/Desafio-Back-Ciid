from fastapi import FastAPI
from router.router import persona_prov
from fastapi.middleware.cors import CORSMiddleware

""" instancia """

app= FastAPI()

origins = [
    "http://localhost.tiangolo.com",
    "https://localhost.tiangolo.com",
    "http://localhost",
    "http://localhost:8080",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)   

app.include_router(persona_prov)
