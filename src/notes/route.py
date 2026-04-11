from fastapi import APIRouter , Depends , Form , Header
from sqlalchemy.orm import Session
from src.notes.model import Note
from src.database.config import get_db
from src.notes.controller import NoteController
from src.users.route import get_current_user
from src.users.model import User

router = APIRouter()

# ----- Method to get the current -------



@router.post('/add')
def add(
        title:str = Form(...),
        content:str = Form(...),
        current_user:User = Depends(get_current_user),
        db:Session = Depends(get_db)
):

    new_note = Note(
        title = title,
        content = content,
        user_id = current_user.id
    )

    return NoteController.add(new_note,db)

@router.delete('/delete')
def delete(
        id:int = Header(...),
        current_user:User = Depends(get_current_user),
        db:Session = Depends(get_db)
):

    return NoteController.delete(id,current_user.id,db)


@router.put('/update')
def update(
        id:int = Header(...),
        title:str = Form(None),
        content:str = Form(None),
        current_user:User = Depends(get_current_user),
        db:Session = Depends(get_db)
):

    return NoteController.put(id , current_user.id,title,content,db)