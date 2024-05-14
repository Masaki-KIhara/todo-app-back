from fastapi import FastAPI,Depends
from typing import List
from .database import SessionLocal, engine 
from . import models, schemas,crud
from sqlalchemy.orm import Session

models.Base.metadata.create_all(bind=engine)

app = FastAPI()

def get_db():
    db=SessionLocal()
    try:
        yield db
    finally:
        db.close()
    
@app.get("/tasks",response_model=List[schemas.BaseTask])
async def read_tasks(db:Session = Depends(get_db),skip:int=0,limit:int=100):
    tasks = crud.get_tasks(db=db, skip=skip, limit=limit)
    return tasks

@app.post("/register_task", response_model=schemas.CreateTask)
async def create_task(item:schemas.CreateTask,db:Session = Depends(get_db)):
    return crud.create_task(db=db,item=item)

@app.delete("/delete_task/{item_id}",response_model=List[schemas.BaseTask])
async def delete_task(item_id:int,db:Session=Depends(get_db)):
    return crud.delete_task(db=db,item_id=item_id)

