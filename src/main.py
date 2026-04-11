from fastapi import FastAPI , Request , Depends
from fastapi.templating import Jinja2Templates

from src.notes.model import Note
from src.notes.route import router as notes_router
from src.users.route import router as user_router
from src.database.config import Base , engine
from sqlalchemy.orm import Session
from src.database.config import get_db
import uvicorn


Base.metadata.create_all(engine)
app = FastAPI()

app.include_router(notes_router, prefix="/notes", tags=["notes"])
app.include_router(user_router, prefix="/users", tags=["users"])
templates = Jinja2Templates(directory="./src/templates")


# ---------- Helper methods right here just to give it  aid with the proccess right here ---- #
# Fixed Render Function
def render(template: str, request: Request):

    return templates.TemplateResponse({'request': request}, template)

# ------- ROUTES ----- #

@app.get('/')
def home(
        request: Request,
) : return render('index.html',request)

@app.get('/register')
def register(
        request:Request,
):
    return render('register.html',request)

@app.get('/main')
def main(
        request:Request,

):
    return render('main.html',request)
@app.get('/notes')
def get_all(
        request: Request,
        db:Session = Depends(get_db)
):

    notes = db.query(Note).all()

    return [ note.to_dict() for note in notes ]

if __name__ == '__main__':
    uvicorn.run(app)

