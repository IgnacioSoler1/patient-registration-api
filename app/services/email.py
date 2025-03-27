import smtplib
from email.message import EmailMessage
import os
import asyncio
from dotenv import load_dotenv

# Cargar variables de entorno
load_dotenv()

MAILTRAP_USER = os.getenv("MAILTRAP_USER")
MAILTRAP_PASS = os.getenv("MAILTRAP_PASS")
MAILTRAP_HOST = os.getenv("MAILTRAP_HOST", "sandbox.smtp.mailtrap.io")
MAILTRAP_PORT = 587  

print("Print de MAILTRAP_USER: ", )
print(MAILTRAP_USER, flush=True)

def send_email_sync(to_email: str, subject: str, body: str):
    """Función síncrona para enviar el correo"""
    msg = EmailMessage()
    msg["Subject"] = subject
    msg["From"] = "hello@demomailtrap.co"
    msg["To"] = to_email
    msg.set_content(body)

    try:
        with smtplib.SMTP(MAILTRAP_HOST, MAILTRAP_PORT) as server:
            server.starttls()  # Asegura la conexión
            server.login(MAILTRAP_USER, MAILTRAP_PASS)
            server.send_message(msg)
    except Exception as e:
        print(f"Error enviando el email: {e}")

async def send_email(to_email: str, subject: str, body: str):
    """Función asíncrona que delega la tarea a un hilo separado"""
    await asyncio.to_thread(send_email_sync, to_email, subject, body)

async def send_confirmation_email(to_email: str):
    """Envía un email de confirmación de manera asíncrona sin bloquear la API"""
    subject = "Registro exitoso"
    body = "Tu registro fue exitoso. Gracias por unirte."
    print(f"Enviando email a {to_email}", flush=True)
    await send_email(to_email, subject, body)




