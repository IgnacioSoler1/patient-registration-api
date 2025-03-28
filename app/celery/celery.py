from celery import Celery
import os

# Cargar la configuración del archivo .env
from dotenv import load_dotenv
load_dotenv()

# Crear la instancia de Celery
celery_app = Celery(
    "patient_registration",  # Nombre de la aplicación
    broker=os.getenv("CELERY_BROKER_URL"),  # Dirección de Redis
    backend=os.getenv("CELERY_RESULT_BACKEND")  # Almacenamiento de resultados (opcional)
)

# Cargar configuración adicional
celery_app.config_from_object("app.config")  # Puedes añadir más configuraciones aquí si lo necesitas
celery_app.autodiscover_tasks(["app.services.email"])  # Descubre las tareas en el archivo de email
