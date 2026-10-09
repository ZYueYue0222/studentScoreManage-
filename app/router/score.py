from sys import exception
from typing import Optional
from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from sqlalchemy import or_
from app.get_db import get_db
from app.models import StudentScore
from app.pydantic_model import StudentScoreCreate,StudentScoreRead,StudentScoreUpdate
from app.pagination import pagination

router=APIRouter()
# 渲染
@router.get("/list")
def getlist(
    keyword:Optional[str]=None,
    pages = Depends(pagination),
    db:Session=Depends(get_db)
):
    res=db.query(StudentScore)
    if keyword:
        res=res.filter(or_(StudentScore.name.like(f"%{keyword}%"),StudentScore.classname.like(f"%{keyword}%")))
    total=res.count()
    data=res.offset(pages["skip"]).limit(pages["pageSize"]).all()
    return {"total":total,"data":data}
# 新增
@router.post("/add",status_code=status.HTTP_201_CREATED)
def add_student(form:StudentScoreCreate,db:Session=Depends(get_db)):
    res=StudentScore(**form.model_dump())
    db.add(res)
    db.commit()
    db.refresh(res)
    return {"msg":"新增成功","data":res}
# 修改
@router.put("/edit/{id}")
def edit_student(id:int,form:StudentScoreUpdate,db:Session=Depends(get_db)):
    res=db.query(StudentScore).get(id)
    if not res:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail="未找到该学生")
    info=form.model_dump(exclude_unset=True)
    for k,v in info.items():
        setattr(res,k,v)
    db.commit()
    db.refresh(res)
    return {"msg":"修改成功","data":res}
# 删除
@router.delete("/delete/{id}")
def delete_student(id:int,db:Session=Depends(get_db)):
    res=db.query(StudentScore).get(id)
    if not res:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail="未找到该学生")
    db.delete(res)
    db.commit()
    return {"msg":"删除成功"}
# 详情
@router.get("/get_one/{id}",response_model=StudentScoreRead)
def get_one(id:int,db:Session=Depends(get_db)):
    res=db.query(StudentScore).get(id)
    if not res:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail="未找到该学生")
    return res