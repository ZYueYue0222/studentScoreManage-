from pydantic import BaseModel
from typing import Optional

class StudentScoreCreate(BaseModel):
    bh:str
    name:str
    age:int
    classname:str
    score:str

class StudentScoreUpdate(BaseModel):
    bh:str|None=None
    name:str|None=None
    age:int|None=None
    classname:str|None=None
    score:str|None=None

class StudentScoreRead(BaseModel):
    id:int
    bh:str
    name:str
    age:int
    classname:str
    score:str
    model_config={"from_attributes":True}