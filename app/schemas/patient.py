from pydantic import BaseModel, EmailStr, HttpUrl

class PatientCreate(BaseModel):
    name: str
    email: EmailStr
    phone: str
    document_url: HttpUrl  # Cambiamos UploadFile por HttpUrl

class PatientResponse(BaseModel):
    id: int
    name: str
    email: EmailStr
    phone: str
    document_url: str

    class Config:
        from_attributes = True
