from src.database.config import Base
from sqlalchemy import Column, Integer, String , DateTime
from datetime import datetime


class Note(Base):

    __tablename__ = 'notes'

    id = Column(Integer , primary_key = True , autoincrement = True  , nullable = False)
    title = Column(String(200) , nullable = False , index = True)
    content = Column(String(1024),  nullable = False , index = True)
    created_at = Column(DateTime, nullable = False , index = True , default=datetime.now())

    def to_dict(self):

        return {
            'id' : self.id,
            'title' : self.title,
            'content' : self.content,
            'created_at' : self.created_at
        }