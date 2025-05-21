import os

class Config:
    SECRET_KEY = os.environ.get('SECRET_KEY', 'sua-chave-secreta')
    
    # Configuração local (PostgreSQL local, comentada)
    # SQLALCHEMY_DATABASE_URI = 'postgresql://postgres:password@localhost/task_manager'
    
    # Configuração Supabase (Direct Connection)
    SQLALCHEMY_DATABASE_URI = 'postgresql://postgres:xcCAq-kuUa.5p?!@db.ixktkhrsubpqctyhbjmb.supabase.co:5432/postgres'
    
    SQLALCHEMY_TRACK_MODIFICATIONS = False