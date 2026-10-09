from sqlalchemy import Column,INTEGER,String
from .get_db import Base


class StudentScore(Base):
    __tablename__="studentscore"
    id=Column(INTEGER,primary_key=True,autoincrement=True)
    bh=Column(String(50),nullable=False)
    name=Column(String(50),nullable=False)
    age=Column(INTEGER,nullable=False)
    classname=Column(String(50),nullable=False)
    score=Column(String(50),nullable=False)
