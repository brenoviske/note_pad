from fastapi import APIRouter , Depends , Form , Header
from sqlalchemy.orm import Session
from src.notes.model import Note
from src.database.config import get_db
from src.notes.controller import NoteController

router = APIRouter()

# ----- Method to get the current -------



@router.post('/add')
def add(
        title:str = Form(...),
        content:str = Form(...),
        db:Session = Depends(get_db)
):

    new_note = Note(
        title = title,
        content = content,
    )

    return NoteController.add(new_note,db)

@router.delete('/delete')
def delete(
        id:int = Header(...),
        db:Session = Depends(get_db)
):

    return NoteController.delete(id,db)


@router.put('/update')
def update(
        id:int = Header(...),
        title:str = Form(None),
        content:str = Form(None),
        db:Session = Depends(get_db)
):

    return NoteController.put(id,title,content,db)