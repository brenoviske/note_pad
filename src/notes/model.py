from sqlalchemy.orm import relationship
from src.database.config import Base
from sqlalchemy import Column, Integer, String , DateTime , ForeignKey , Enum
from datetime import datetime


class Note(Base):

    __tablename__ = 'notes'

    id = Column(Integer , primary_key = True , autoincrement = True  , nullable = False)
    title = Column(String(200) , nullable = False , index = True)
    content = Column(String(1024),  nullable = False , index = True)
    status = Column(Enum('Completed ', 'Pending ', 'Canceled'), nullable = False , index = True)
    priority = Column(Enum('High', 'Medium','Low'), nullable = False , index = True)
    created_at = Column(DateTime, nullable = False , index = True , default=datetime.now())

    user_id = Column(Integer, ForeignKey('users.id') , nullable = False)
    user = relationship('User', back_populates = 'notes')

    def to_dict(self):

        return {
            'id' : self.id,
            'title' : self.title,
            'content' : self.content,
            'created_at' : self.created_at
        }