from fastapi import HTTPException
from sqlalchemy.orm import Session
from . import models,schemas

# def get_users(db:Session,skip:int=0,limit:int=100):
#     return db.query(models.User).offset(skip).limit(limit).all()

# def create_user(db:Session,):
#     return ""

# def update_user(db:Session,):
#     return ""

def get_tasks(db:Session,skip:int=0,limit:int=100):
    return db.query(models.Task).offset(skip).limit(limit).all()

def create_task(db:Session,item:schemas.CreateTask):
    db_task = models.Task(title=item.title)
    db.add(db_task)
    db.commit()
    db.refresh(db_task)
    return db_task

def delete_task(db:Session,item_id:int):
    db_task = db.query(models.Task).filter(models.Task.id == item_id).first()
    if db_task is None:
        raise HTTPException(status_code=404, detail="Task not found.")
    db.delete(db_task)
    db.commit()
    return db.query(models.Task).offset(0).limit(100).all()

def update_task(db:Session,item_id:int,item:schemas.UpdateTask):
    db_task:schemas.UpdateTask = db.query(models.Task).filter(models.Task.id == item_id).one()
    db_task.title = item.title
    db_task.is_complete = item.is_complete
    db.commit()
    return db.query(models.Task).offset(0).limit(100).all()