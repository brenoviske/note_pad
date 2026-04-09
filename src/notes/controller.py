from src.notes.repo import NoteRepo
from src.notes.model import Note
from sqlalchemy.orm import Session

class NoteController:

    @staticmethod
    def add(new_note:Note,db:Session):

        return NoteRepo.add(new_note,db)

    @staticmethod
    def delete(id:int,db:Session):

        return NoteRepo.delete(id,db)

    @staticmethod
    def put(id:int , title:str , content:str , db:Session):

        return NoteRepo.put(id,title,content,db)