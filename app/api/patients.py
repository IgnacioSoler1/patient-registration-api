import asyncio
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.db.database import get_db
from app.models.patient import Patient
from app.schemas.patient import PatientCreate, PatientResponse
from app.services.email_service import send_confirmation_email
from app.services.base import NotificationManager
from typing import List

router = APIRouter()
# Ruta para crear paciente. Verifica que los datos ingresados sean coherentes con lo definido en /schemas/patient.py
# Crea el objeto paciente y lo guarda en la base de datos.
# Llama la funcion para enviar mail de bienvenida.
@router.post("/register", response_model=PatientResponse)
async def register_patient(patient_data: PatientCreate, db: Session = Depends(get_db)):
    existing_patient = db.query(Patient).filter(Patient.email == patient_data.email).first()
    if existing_patient:
        raise HTTPException(status_code=400, detail="Email already registered")

    new_patient = Patient(
        name=patient_data.name,
        email=patient_data.email,
        phone=patient_data.phone,
        document_url=patient_data.document_url
    )
    db.add(new_patient)
    db.commit()
    db.refresh(new_patient)

    print(f"📧 Enviando email de confirmación a {patient_data.email}", flush=True)
    notification_manager = NotificationManager()
    notification_manager.send_notification(
        type='email', 
        recipient=patient_data.email, 
        message="Tu registro fue exitoso. Gracias por unirte."
    )

    return new_patient

# Devuelve todos los pacientes creados
@router.get("/getPatients", response_model=List[PatientResponse])
def get_patients(db: Session = Depends(get_db)):
    """Obtiene la lista de todos los pacientes registrados en la base de datos."""
    patients = db.query(Patient).all()
    return patients

#Devuelve los datos del paciente con la id ingresada
@router.get("/getPatientById/{patient_id}", response_model=PatientResponse)
def get_patient_by_id(patient_id: int, db: Session = Depends(get_db)):
    """Obtiene un paciente por su ID."""
    patient = db.query(Patient).filter(Patient.id == patient_id).first()
    if not patient:
        raise HTTPException(status_code=404, detail="Paciente no encontrado")
    return patient

# Elimina el registro del paciente con la id ingresada
@router.post("/deletePatientById/{patient_id}")
def delete_patient_by_id(patient_id: int, db: Session = Depends(get_db)):
    """Elimina un paciente por su ID."""
    patient = db.query(Patient).filter(Patient.id == patient_id).first()
    if not patient:
        raise HTTPException(status_code=404, detail="Paciente no encontrado")
    
    db.delete(patient)
    db.commit()
    return {"message": f"Paciente con ID {patient_id} eliminado correctamente"}
