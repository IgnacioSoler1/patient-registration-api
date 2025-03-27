from fastapi import APIRouter, Depends, HTTPException, UploadFile, File
from sqlalchemy.orm import Session
from app.db.database import get_db
from app.models.patient import Patient
from app.schemas.patient import PatientCreate, PatientResponse
from app.services.email import send_confirmation_email
import os
from typing import List
import asyncio

router = APIRouter()

UPLOAD_DIR = "uploads/"
os.makedirs(UPLOAD_DIR, exist_ok=True)

@router.post("/register", response_model=PatientResponse)
async def register_patient(
    patient_data: PatientCreate,
    db: Session = Depends(get_db)
):
    # Verificar si el email ya está registrado
    existing_patient = db.query(Patient).filter(Patient.email == patient_data.email).first()
    if existing_patient:
        raise HTTPException(status_code=400, detail="Email already registered")

    # Guardar en la base de datos
    new_patient = Patient(
        name=patient_data.name,
        email=patient_data.email,
        phone=patient_data.phone,
        document_url=patient_data.document_url  # Ahora almacenamos una URL en vez de un archivo
    )
    db.add(new_patient)
    db.commit()
    db.refresh(new_patient)

    print("llamamos la funcion de enviar email", flush=True)
    # Enviar email en segundo plano SIN BLOQUEAR la respuesta
    asyncio.create_task(send_confirmation_email(patient_data.email))

    return new_patient


@router.get("/list", response_model=List[PatientResponse])
def get_patients(db: Session = Depends(get_db)):
    """Obtiene la lista de todos los pacientes registrados en la base de datos."""
    patients = db.query(Patient).all()
    return patients