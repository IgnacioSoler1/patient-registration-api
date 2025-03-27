import smtplib
from email.mime.text import MIMEText
import os
import asyncio
from dotenv import load_dotenv

# Cargar variables de entorno
load_dotenv()

GMAIL_USER = os.getenv("GMAIL_USER")  # Tu dirección de Gmail
GMAIL_PASS = os.getenv("GMAIL_PASS")  # Contraseña de aplicación generada en Google

def send_email_sync(to_email: str, subject: str, body: str):
    """Función síncrona para enviar el correo a cualquier destinatario"""
    msg = MIMEText(body)
    msg["Subject"] = subject
    msg["From"] = GMAIL_USER
    msg["To"] = to_email

    try:
        with smtplib.SMTP_SSL("smtp.gmail.com", 465) as server:
            server.login(GMAIL_USER, GMAIL_PASS)
            server.sendmail(GMAIL_USER, [to_email], msg.as_string())
            print(f"✅ Email enviado a {to_email}", flush=True)
    except Exception as e:
        print(f"❌ Error enviando el email: {e}", flush=True)

async def send_email(to_email: str, subject: str, body: str):
    """Función asíncrona que delega el envío a un hilo separado"""
    await asyncio.to_thread(send_email_sync, to_email, subject, body)

async def send_confirmation_email(to_email: str):
    """Envía un email de confirmación"""
    subject = "Registro exitoso"
    body = "Tu registro fue exitoso. Gracias por unirte."
    await send_email(to_email, subject, body)





