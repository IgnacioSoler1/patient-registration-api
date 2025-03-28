from locust import HttpUser, task, between
from faker import Faker

fake = Faker()

class PatientLoadTest(HttpUser):
    wait_time = between(3, 5)

    @task
    def create_patient(self):
        payload = {
            "name": fake.name(),
            "email": fake.unique.email(),
            "phone": fake.phone_number(),
            "document_url": fake.url()
        }
        response = self.client.post("/patients/register", json=payload)
        print(response.status_code, response.text)
