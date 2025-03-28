Patient Registration API
========================

Este es un proyecto de API para el registro de pacientes, desarrollado con FastAPI y SQLAlchemy. Permite registrar pacientes, almacenar sus datos y enviar correos electrónicos de confirmación.

📁 Estructura del Proyecto
--------------------------

```
PATIENT-REGISTRATION-API/
│── app/
│   ├── api/
│   │   ├── patients.py    # Endpoints de la API
│   ├── db/
│   │   ├── database.py    # Configuración de la base de datos
│   ├── models/
│   │   ├── patient.py     # Definición del modelo de datos
│   ├── schemas/
│   │   ├── patient.py     # Esquemas Pydantic para validación de datos
│   ├── services/
│   │   ├── email.py       # Servicio de envío de correos electrónicos
│   ├── config.py          # Configuración del proyecto
│   ├── main.py            # Punto de entrada de la API
│── .env                   # Variables de entorno
│── .gitignore             # Archivos ignorados por Git
│── compose.yaml           # Configuración para Docker Compose
│── Dockerfile             # Dockerización del proyecto
│── README.md              # Documentación del proyecto
│── requirements.txt       # Dependencias del proyecto
```

🚀 Instalación y Configuración
------------------------------

### 1️⃣ Clonar el repositorio

Plain `   git clone https://github.com/tu-usuario/patient-registration-api.git  cd patient-registration-api   `

### 2️⃣ Crear entorno virtual e instalar dependencias

Plain ``   python3 -m venv env  source env/bin/activate  # En Windows usa `env\Scripts\activate`  pip install -r requirements.txt   ``

### 3️⃣ Configurar variables de entorno

Renombrar el archivo .env.example a .env y completar los valores necesarios.

### 4️⃣ Ejecutar la API

Plain `   uvicorn app.main:app --reload   `

La API estará disponible en http://127.0.0.1:8000.

## 🛠️ Endpoints Principales

### 📍 Registro de Paciente

**POST** `/register`

* *   **Descripción**: Registra un nuevo paciente en la base de datos.
*     
* *   **Payload:**
*     
*     ```
*     {
*       "name": "John Doe",
*       "email": "john@example.com",
*       "phone": "+1234567890",
*       "document_blob": "archivo_binario"
*     }
*     ```
*     
* *   **Respuesta:**
*     
*     ```
*     {
*       "id": 1,
*       "name": "John Doe",
*       "email": "john@example.com",
*       "phone": "+1234567890"
*     }
*     ```
*     

### 📍 Obtener Pacientes

**GET** `/patients`

* *   **Descripción**: Devuelve la lista de pacientes registrados.
*     
* *   **Respuesta:**
*     
*     ```
*     [
*       {
*         "id": 1,
*         "name": "John Doe",
*         "email": "john@example.com"
*       }
*     ]
*     ```
*     

### 📍 Obtener un Paciente por ID

**GET** `/patients/{id}`

* *   **Descripción**: Retorna los detalles de un paciente específico.
*     

### 📍 Eliminar un Paciente

**DELETE** `/patients/{id}`

* *   **Descripción**: Elimina un paciente de la base de datos.
*     

* * *

## 📧 Servicio de Envío de Correos

El servicio `email.py` usa `smtplib` para enviar correos electrónicos de confirmación a los pacientes.

```
import smtplib
from email.mime.text import MIMEText

def send_email(subject, body, recipient):
    msg = MIMEText(body)
    msg["Subject"] = subject
    msg["From"] = "noreply@miapp.com"
    msg["To"] = recipient
    with smtplib.SMTP_SSL("smtp.gmail.com", 465) as smtp:
        smtp.login("tu_email@gmail.com", "tu_password")
        smtp.sendmail("noreply@miapp.com", recipient, msg.as_string())
    print("📧 Email enviado con éxito")
```

* * *

## 🐳 Dockerización

Si deseas correr el proyecto con Docker, usa:

```
docker-compose up --build
```

Esto levantará un contenedor con la API y la base de datos PostgreSQL.

* * *