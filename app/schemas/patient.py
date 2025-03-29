from pydantic import BaseModel, EmailStr, HttpUrl

#Definimos las respuestas que esperamos en las API's
class PatientCreate(BaseModel):
    name: str
    email: EmailStr
    phone: str
    document_url: HttpUrl  

class PatientResponse(BaseModel):
    id: int
    name: str
    email: EmailStr
    phone: str
    document_url: str

    class Config:
        from_attributes = True
