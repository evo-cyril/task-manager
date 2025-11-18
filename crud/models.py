from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.automap import automap_base
from pydantic import BaseModel

DATABASE_URI = 'postgresql://postgres:akzpass@localhost:5432/akshay'

engine = create_engine(DATABASE_URI)

Base = automap_base()
Base.prepare(engine, reflect=True)

Crud_op = Base.classes.crud_op   # table name must be lower-case

SessionLocal = sessionmaker(bind=engine, autocommit=False, autoflush=False)
session = SessionLocal()

# Pydantic models should only be in the models.py file 
class Createtask(BaseModel):
    title: str
    isdone:bool = False
    is_active:bool = True
class updatetask(BaseModel):
    id:int
    isdone:bool
class deletetask(BaseModel):
    id:int      


print("DB Configured Successfully...")
