from abc import ABC, abstractmethod
from typing import Dict, Any
from app.services.email_service import send_confirmation_email

class NotificationService(ABC):
    @abstractmethod
    def send(self, recipient: str, message: str, **kwargs) -> None:
        """Método abstracto para enviar notificaciones"""
        pass

class EmailNotificationService(NotificationService):
    def send(self, recipient: str, message: str, **kwargs) -> None:
        # Lógica de envío de email usando Celery
        send_confirmation_email(recipient, message)

class SMSNotificationService(NotificationService):
    def send(self, recipient: str, message: str, **kwargs) -> None:
        # Futura implementación de SMS con cola de mensajes
        # Podrías usar una tarea de Celery similar a send_confirmation_email
        print(f"Enviando SMS a {recipient}: {message}")
        # Ejemplo: sms_task.delay(recipient, message)

class NotificationManager:
    def __init__(self):
        self.services: Dict[str, NotificationService] = {
            'email': EmailNotificationService(),
            # 'sms': SMSNotificationService()  # Descomentar cuando implementes SMS
        }

    def get_service(self, type: str) -> NotificationService:
        return self.services.get(type)

    def send_notification(self, type: str, recipient: str, message: str, **kwargs):
        service = self.get_service(type)
        if service:
            service.send(recipient, message, **kwargs)
        else:
            raise ValueError(f"Servicio de notificación {type} no encontrado")