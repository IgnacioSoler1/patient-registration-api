from sqlalchemy import Column, Integer, String
from app.db.database import Base

#Definimos entidad de paciente para la base de datos.
class Patient(Base):
    __tablename__ = "patients"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(255), nullable=False)
    email = Column(String(255), unique=True, nullable=False)
    phone = Column(String(255), nullable=False)
    document_url = Column(String(255), nullable=False)  # Almacenamos una URL para la foto

