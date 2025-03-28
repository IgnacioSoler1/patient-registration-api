import smtplib
from email.mime.text import MIMEText
import os
import asyncio
from dotenv import load_dotenv
from celery import shared_task

# Cargar variables de entorno
load_dotenv()

GMAIL_USER = os.getenv("GMAIL_USER")  # Tu dirección de Gmail
GMAIL_PASS = os.getenv("GMAIL_PASS")  # Contraseña de aplicación generada en Google

# Definir la tarea de Celery para enviar el email
@shared_task(bind=True, max_retries=3)
def send_email_sync(self, to_email: str, subject: str, body: str):
    """Función síncrona para enviar un correo electrónico utilizando SMTP"""
    msg = MIMEText(body)
    msg["Subject"] = subject
    msg["From"] = GMAIL_USER
    msg["To"] = to_email

    try:
        with smtplib.SMTP_SSL("smtp.gmail.com", 465) as server:
            server.login(GMAIL_USER, GMAIL_PASS)
            server.sendmail(GMAIL_USER, [to_email], msg.as_string())
            print(f"✅ Email enviado a {to_email}")
    except Exception as e:
        print(f"❌ Error enviando el email a {to_email}: {e}")
        raise self.retry(exc=e, countdown=60)  # Reintentar en 60s

# Función que se invoca para delegar el envío del correo a Celery
def send_confirmation_email(to_email: str, body: str):
    """Envía un email de confirmación usando Celery"""
    subject = "Registro exitoso"
    send_email_sync.apply_async(args=[to_email, subject, body])