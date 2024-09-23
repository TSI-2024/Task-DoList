
import os

class Config:
    # Configuración de la base de datos
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or 'postgresql://usuario:contraseña@localhost/nombre_base_datos'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
