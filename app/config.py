import os

class Config:
    SECRET_KEY = os.environ.get('SECRET_KEY', 'sua-chave-secreta')
    SQLALCHEMY_DATABASE_URI = 'postgresql://postgres:password@localhost/task_manager'
    SQLALCHEMY_TRACK_MODIFICATIONS = False