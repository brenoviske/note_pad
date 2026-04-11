from src.database.config import Base
from sqlalchemy.orm import relationship
from sqlalchemy import Column, Integer, String, ForeignKey , DateTime
from datetime import datetime

class User(Base):

    __tablename__ = 'users'

    id = Column(Integer, primary_key=True, autoincrement=True , nullable=False)
    email = Column(String, unique=True, nullable=False)
    username = Column(String(200), nullable = False , index=True)
    password_hash = Column(String(200), nullable = False , index=True)
    created_at = Column(DateTime, nullable=False, default=datetime.utcnow)

    notes = relationship('Note', back_populates='user', cascade='all, delete-orphan')  # New relationship established now between the Note table and the User table

    def to_dict(self):

        return {
            'id':self.id,
            'email':self.email,
            'username':self.username,
            'created_at':self.created_at,

        }