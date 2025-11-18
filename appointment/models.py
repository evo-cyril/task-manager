from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from  sqlalchemy.ext.automap import automap_base
from pydantic import BaseModel


DATABASE_URI = 'postgresql://postgres:akzpass@localhost:5432/akshay'

engine=create_engine(DATABASE_URI,echo=True)
Base = automap_base()
Base.prepare(engine,reflect=True)

print("Mapped Tables:", Base.classes.keys())

sessionlocal=sessionmaker(bind=engine, autocommit=False, autoflush=False)
session=sessionlocal()

#connecting tables

doc = Base.classes.doctor
pat = Base.classes.patient
apo = Base.classes.Appointment

# pydantics

class create_app(BaseModel):

    id : str
    d_id : str
    patient_name : str
    completed : bool = False

class view_app(BaseModel):

    id : str
    d_id : str
    patient_name : str
    completed : bool        