# importo librerias.
from fastapi import FastAPI
import uvicorn
import streamlit as st

# inicializo la api.

app = FastAPI()

@app.get("/")
def saludo():
    return {"Mensaje":"Dale Boca!"}
