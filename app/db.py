from sqlalchemy import create_engine, Column, Integer, String, Text, DateTime
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from datetime import datetime

Base = declarative_base()

class Dossier(Base):
    __tablename__ = 'dossiers'
    id = Column(Integer, primary_key=True)
    nom = Column(String)
    date = Column(DateTime, default=datetime.utcnow)
    motif = Column(Text)
    statut = Column(String, default="En cours")

engine = create_engine('sqlite:///app/dossiers.db')
Session = sessionmaker(bind=engine)
Base.metadata.create_all(engine)
