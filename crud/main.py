from fastapi import FastAPI, Depends, HTTPException
from pydantic import BaseModel
from fastapi.responses import JSONResponse
from models import Crud_op, session   # from your models.py

app = FastAPI(title="crud api")

class CreateCrud(BaseModel):
    title: str
    isdone: list[str]

# @app.post("/cruds/")
# def create_task(task: CreateCrud):
#     new_task = Crud_op(title=task.title, isdone=task.isdone)
#     session.add(new_task)
#     session.commit()
#     session.refresh(new_task)
#     return new_task

@app.get("/cruds/")
def view_task():
    view=session.query(Crud_op).all()
    return view