from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine
from pydantic import BaseModel


Base = automap_base()

DATABASE_URI = 'postgresql://postgres:akzpass@localhost:5432/akshay'


engine = create_engine(DATABASE_URI, echo=True)
SessionLocal = sessionmaker(bind=engine)
session = SessionLocal()

Task = Base.classes.crud_op

Base.metadata.create_all(bind=engine)


class TaskCreate(BaseModel):
    title: str

class TaskUpdate(BaseModel):
    id: int
    is_done: bool

class TaskDelete(BaseModel):
    id: int