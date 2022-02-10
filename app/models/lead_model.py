from dataclasses import dataclass
from datetime import datetime
from sqlalchemy import Column, String, DateTime, Integer
from app.configs.database import db


@dataclass
class LeadModel(db.Model):
    __tablename__ = "leads"

    id = Column(Integer, primary_key=True)
    name: str = Column(String, nullable=False)
    email: str = Column(String, unique=True, nullable=False)
    phone: str = Column(String, unique=True, nullable=False)
    creation_date: datetime = Column(DateTime, default=datetime.now())
    last_visit: datetime = Column(DateTime, default=datetime.now())
    visits: int = Column(Integer, default=1)
