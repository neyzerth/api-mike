# main.py
from contextlib import asynccontextmanager
from fastapi import FastAPI

#Importacion de archivos previos
from db.database import create_db_and_tables
from api.v1.user_api import *
# from core.cors import setup_cors


"""
Antes usábamos @app.on_event("startup"), pero FastAPI ahora prefiere usar un gestor
"""
@asynccontextmanager
async def lifespan(app: FastAPI):
    # Startup: Se ejecuta al iniciar
    print("Iniciando base de datos...")
    create_db_and_tables()
    yield
    # Shutdown: Se ejecuta al cerrar (aqui podrías cerrar conexiones)
    print("Cerrando aplicación...")

# Crear la app con lifespan
app = FastAPI(
    title="FastAPI Mike",
    description="Mi primera API con FastAPI y SQLModel",
    version="1.0.0",
    lifespan=lifespan  # <-- Aquí está el cambio clave
)

# setup_cors(app)

@app.get("/")
def root():
    return {"message": "¡Bienvenido a FastAPI Mike!"}


@app.get("/health")
def health_check():
    return {"status": "healthy"}
