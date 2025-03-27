import os
from dotenv import load_dotenv

load_dotenv()

class Settings:
    DATABASE_URL = os.getenv("DATABASE_URL", "mysql+pymysql://root:password@db/patient_db")
    EMAIL_USER = os.getenv("EMAIL_USER", "your_mailtrap_user")
    EMAIL_PASS = os.getenv("EMAIL_PASS", "your_mailtrap_pass")

settings = Settings()
