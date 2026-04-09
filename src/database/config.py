from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base , sessionmaker
from dotenv import load_dotenv
import os

load_dotenv()

db_url = os.getenv("db_url")
engine = create_engine(db_url)
Base = declarative_base()

Session = sessionmaker(bind=engine)

def get_db():

    db = Session()

    try:yield db
    except Exception as e:
        db.rollback()
        raise e
    finally:db.close()