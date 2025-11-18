# You havent used Depends and HTTPException, Then why import it
from fastapi import FastAPI, Depends, HTTPException
# JSONResponse is imported, where is it used?
from fastapi.responses import JSONResponse

from models import Crud_op, session, Createtask ,updatetask,deletetask # from your models.py

app = FastAPI(title="crud api")


    
# # cruds? API names should be meaningful
# @app.post("/create/") 
# def create_task(task: Createtask):
#     new_task = Crud_op(
#         title=task.title,
#         isdone=task.isdone,
#         is_active=task.is_active)
#     session.add(new_task)
#     session.commit()
#     session.refresh(new_task)
#     data = {
#         "id":new_task.id,
#         "title":new_task.title,
#         "isdone":new_task.isdone
#     }

#     return JSONResponse({ 
#         "status": True,
#         "message": "Task created successfully",
#         "data": data

#     # })
# @app.get("/list/")
# def view_task():
#     task=session.query(Crud_op)
#     count=task.count()
#     if count < 1:
#         return JSONResponse({
#             "status": False,
#             "message": "No Tasks Available",
#             "data": []
#         })
#     task=task.all()
#     data=[]
#     for t in task:
#         data.append({
#             "id":t.id,
#             "title":t.title,
#             "isdone":t.isdone
           
#         })
#     return JSONResponse({
#         "status":True,
#         "message":"listed successfully",
#         "data":data

#         })

        
    
#     # You shouldnt directly return this. Thats why JSONResponse is used
    







#update a task
# @app.put("/update/{data_id}")
# def update_task(data:updatetask,data_id : int):
#     task=session.query(Crud_op).filter(Crud_op.id == data_id).first()
#     if not task:
#         return JSONResponse({
#             "status":False,
#             "message":"Task not Founded"
#         })
#     task.isdone = data.isdone
#     session.add(task)
#     session.commit()
#     session.refresh(task)

#     output = {
#         "id": task.id,
#         "title": task.title,
#         "is_done": task.isdone
#     }
    
#     return JSONResponse({
#         "status":True,
#         "message":"updated successfully",
#         "data":output
#     })
#delete

@app.delete("/delete/{del_id}")
def deletetask(del_id : int ):
    task=session.query(Crud_op).filter(Crud_op.id == del_id).first()
    if not task:
        return JSONResponse({
            "status":False,
            "message":"nothing to delete!!"
        ,
        })    
    session.delete(task)
    session.commit()
    return JSONResponse({
         "status":True,
         "message":"task delete successfully",
    })