from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import List
from datetime import date

app = FastAPI()

class Task(BaseModel):
    id: int
    title: str
    description: str
    due_date: date
    priority: int
    completed: bool

tasks: List[Task] = []

def find_task(task_id: int):
    for task in tasks:
        if task.id == task_id:
            return task
    return None

def get_next_id():
    if not tasks:
        return 1
    return max(task.id for task in tasks) + 1

@app.get("/")
def read_root():
    return {"message": "Welcome to the To-Do application!"}

@app.get("/tasks", response_model=List[Task])
def get_tasks():
    return tasks

@app.post("/tasks", response_model=Task)
def create_task(task: Task):
    task.id = get_next_id()
    tasks.append(task)
    return task

@app.get("/tasks/{task_id}", response_model=Task)
def get_task(task_id: int):
    task = find_task(task_id)
    if task is None:
        raise HTTPException(status_code=404, detail="Task not found")
    return task

@app.put("/tasks/{task_id}", response_model=Task)
def update_task(task_id: int, updated_task: Task):
    task = find_task(task_id)
    if task is None:
        raise HTTPException(status_code=404, detail="Task not found")
    task.title = updated_task.title
    task.description = updated_task.description
    task.due_date = updated_task.due_date
    task.priority = updated_task.priority
    task.completed = updated_task.completed
    return task

@app.delete("/tasks/{task_id}")
def delete_task(task_id: int):
    task = find_task(task_id)
    if task is None:
        raise HTTPException(status_code=404, detail="Task not found")
    tasks.remove(task)
    return {"message": "Task deleted successfully"}

@app.get("/tasks/due/{due_date}", response_model=List[Task])
def get_tasks_by_due_date(due_date: date):
    due_tasks = [task for task in tasks if task.due_date == due_date]
    return due_tasks

@app.get("/tasks/priority/{priority}", response_model=List[Task])
def get_tasks_by_priority(priority: int):
    priority_tasks = [task for task in tasks if task.priority == priority]
    return priority_tasks
