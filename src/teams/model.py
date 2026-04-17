from src.database.config import Base
from sqlalchemy import Column , Integer , String , ForeignKey
from sqlalchemy.orm import relationship


class Team(Base):

    __tablename__ = "teams"

    id = Column(Integer , primary_key=True, nullable=False , autoincrement=True)
    name = Column(String(200), nullable=False, index=True)


    user_id = Column(Integer,  ForeignKey('users.id'), nullable=False, index=True)
    user = relationship('User', back_populates='teams')

    def to_dict(self):

        return {
            'id':self.id,
            'name':self.name,
            'user_id':self.user_id,
        }