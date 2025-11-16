from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.automap import automap_base

DATABASE_URI = 'postgresql://postgres:akzpass@localhost:5432/akshay'

engine = create_engine(DATABASE_URI)

Base = automap_base()
Base.prepare(engine, reflect=True)

Crud_op = Base.classes.crud_op   # table name must be lower-case

SessionLocal = sessionmaker(bind=engine, autocommit=False, autoflush=False)
session = SessionLocal()

print("DB Configured Successfully...")
