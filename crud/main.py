# You havent used Depends and HTTPException, Then why import it
from fastapi import FastAPI, Depends, HTTPException
from pydantic import BaseModel

# JSONResponse is imported, where is it used?
from fastapi.responses import JSONResponse

from models import Crud_op, session   # from your models.py

app = FastAPI(title="crud api")

# Pydantic models should only be in the models.py file 
class CreateCrud(BaseModel):
    title: str
    isdone: list[str]
    
# cruds? API names should be meaningful
# @app.post("/cruds/") 
# def create_task(task: CreateCrud):
#     new_task = Crud_op(title=task.title, isdone=task.isdone)
#     session.add(new_task)
#     session.commit()
#     session.refresh(new_task)  no use of this
#     return new_task

@app.get("/cruds/")
def view_task():
    view=session.query(Crud_op).all()
    # You shouldnt directly return this. Thats why JSONResponse is used
    return view







