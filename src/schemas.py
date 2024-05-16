from pydantic import BaseModel
from datetime import datetime

# class CreateUser(BaseModel):
#     user_name:str
#     email:str
#     password:str


# class BaseUser(CreateUser):
#     id:int

#     class Config:
#         orm_mode = True

class CreateTask(BaseModel):
    title:str 
    is_complete:bool

class DeleteTask(BaseModel):
    id:int


class BaseTask(CreateTask):
    id:int
    created_at:datetime
    # owner_id:int

    class Config:
        orm_mode = True


