from fastapi import Depends , APIRouter , HTTPException , status
from fastapi.security import OAuth2PasswordBearer
from pydantic import BaseModel
from pydantic import EmailStr
from sqlalchemy.orm import Session
from jose import jwt , JWTError

# ------- Imported related to the src folder of the project -----

from src.database.config import get_db
from src.users.controller import UserController
from src.users.model import User
from src.security.auth import hash_password, verify_password, create_access_token , secret_key , ALGORITHM

router = APIRouter()

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="login")


# ------- Instancing here the users pydantic table ---- -

class UserCreate(BaseModel):

    email: EmailStr
    username:str
    password_hash:str

class UserCreated(BaseModel):

    email: EmailStr
    password:str

class UserUpdate(BaseModel):

    email: EmailStr
    username:str

# ------ Getting the current user while using the jwt tokens for it -------

def get_current_user(token: str = Depends(oauth2_scheme), db: Session = Depends(get_db)):

    credentials_exception = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Could not validate credentials",
        headers={"WWW-Authenticate": "Bearer"},
    )
    try:
        # 1. Decode the token using your SECRET_KEY
        payload = jwt.decode(token, secret_key, algorithms=[ALGORITHM])
        email: str = payload.get("sub")  # We stored the email in 'sub' during login
        if email is None:
            raise credentials_exception
    except JWTError:
        raise credentials_exception

    # 2. Query the database using the identity found in the token
    user = db.query(User).filter(User.email == email).first()

    if user is None:
        raise credentials_exception

    return user

@router.post('/add')
def add(
        user: UserCreate,
        db: Session = Depends(get_db),
):

    new_user = User( email = user.email , username = user.username  , password_hash = hash_password(user.password_hash ))

    return UserController.add_user(new_user,db)


@router.post('/login')
def login(user: UserCreated, db: Session = Depends(get_db)):
    existing_email = db.query(User).filter(User.email == user.email).first()

    if existing_email and verify_password(user.password, existing_email.password_hash):
        # Generate the token
        token = create_access_token(data={"sub": existing_email.email})

        return {
            'status': 'success',
            'access_token': token,
            'token_type': 'bearer'
        }

    return {'status': 'error', 'message': 'Invalid Credentials'}

@router.delete('/delete')
def delete(
        current_user:User = Depends(get_current_user),
        db:Session = Depends(get_db),
):

    return UserController.remove_user(current_user.id,db)

@router.put('/update')
def update(
        new_user:UserUpdate,
        current_user:User = Depends(get_current_user),
        db:Session = Depends(get_db),
):

    return UserController.update_user(current_user.id,new_user.email , new_user.username, db)