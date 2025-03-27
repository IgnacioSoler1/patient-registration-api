import sys
import os

# Añade el directorio actual al path de Python
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

from fastapi import FastAPI
from app.api import patients
from app.db.database import Base, engine

# Crear las tablas en la base de datos
Base.metadata.create_all(bind=engine)

app = FastAPI(title="Patient Registration API")

# Incluir las rutas
app.include_router(patients.router, prefix="/patients", tags=["Patients"])

@app.get("/")
def health_check():
    return {"message": "API is running!"}
