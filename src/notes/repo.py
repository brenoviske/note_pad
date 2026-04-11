from src.notes.model import Note
from sqlalchemy.orm import Session

class NoteRepo:

    @staticmethod
    def find_task_perId(id:int , user_id:int , db:Session):
        return db.query(Note).filter(Note.id == id , Note.user_id == user_id).first()

    @staticmethod
    def add(new_note:Note , db:Session):

        try:

            db.add(new_note)
            db.commit()
            db.refresh(new_note)

            return {'status':'success'}

        except Exception as e:

            print('Error',e)
            return {'status':'error','message':'Houve um erro ao adicionar esta nota'}

    @staticmethod
    def delete(id:int , user_id:int, db:Session):

        note = NoteRepo.find_task_perId(id, user_id , db)

        if not note:

            return {'status':'error','message':'Nota nao encontrada'}

        try:

            db.delete(note)
            db.commit()

            return {'status':'success'}

        except Exception as e:

            print('Error',e)
            return {'status':'error','message':str(e)}

    @staticmethod
    def put(id:int , user_id:int, title:str, content:str , db:Session):

        note = NoteRepo.find_task_perId(id , user_id, db)

        if not note :

            return {'status':'error','message':'Nota nao encontrada'}

        try:

            if title: note.title = title
            if content: note.content = content

            db.commit()

            return {'status':'success'}

        except Exception as e:

            print('Error',e)

            return {'status':'error','message':str(e)}


