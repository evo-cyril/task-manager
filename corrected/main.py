from fastapi import FastAPI, HTTPException
from fastapi.responses import JSONResponse
from .models import session, TaskCreate, TaskUpdate, TaskDelete, Task

app = FastAPI(title="Task Manager")


# 1️⃣ Add Task
@app.post("/create")
def create_task(task: TaskCreate):
    new_task = Task(title=task.title)
    session.add(new_task)
    session.commit()
    session.refresh(new_task)

    data = {
        "id": new_task.id,
        "title": new_task.title,
        "is_done": new_task.is_done
    }

    return JSONResponse({
        "status": True,
        "message": "Task created successfully",
        "data": data
    })


# 2️⃣ List Tasks
@app.get("/list")
def list_tasks():
    tasks = session.query(Task)
    count = tasks.count()

    if count < 1:
        return JSONResponse({
            "status": False,
            "message": "No Tasks Available",
            "data": []
        })

    tasks = tasks.all()

    data = []
    for t in tasks:
        data.append({
            "id": t.id,
            "title": t.title,
            "is_done": t.is_done
        })

    return JSONResponse({
        "status": True,
        "message": "Task listed successfully",
        "data": data
    })


# 3️⃣ Update Task Status
@app.put("/update")
def update_task(data: TaskUpdate):
    task = session.query(Task).filter(Task.id == data.id).first()

    if not task:
        return JSONResponse({
            "status": False,
            "message": "Task not found",
            "data": None
        })

    task.is_done = data.is_done
    session.commit()
    session.refresh(task)

    output = {
        "id": task.id,
        "title": task.title,
        "is_done": task.is_done
    }

    return JSONResponse({
        "status": True,
        "message": "Task updated successfully",
        "data": output
    })


# 4️⃣ Delete Task
@app.delete("/delete")
def delete_task(data: TaskDelete):
    task = session.query(Task).filter(Task.id == data.id).first()

    if not task:
        return JSONResponse({
            "status": False,
            "message": "Task not found",
            "data": None
        })

    session.delete(task)
    session.commit()

    return JSONResponse({
        "status": True,
        "message": "Task deleted successfully",
        "data": None
    })
