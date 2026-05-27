from fastapi import APIRouter, Depends
from services.department_service import create_department, update_department, get_all_department, get_single_department, delete_department
from schemas.department import DepartmentSchemas
from core.database import get_db
from sqlalchemy.orm import Session

router = APIRouter(prefix="/department",tags="department")

@router.post("/create-department")
def CreateDepartment(department : DepartmentSchemas,  db: Session = Depends(get_db)):
    return create_department(department, db)

@router.get("/")
def GetDepartments(db:Session = Depends(get_db)):
    return get_all_department(db)

@router.get("/{id}")
def GetSingleDepartment(id: int, db:Session = Depends(get_db)):
    return get_single_department(id,db)

@router.delete("delete-department/{id}")
def DeleteDepartment(id: int, db:Session = Depends(get_db)):
    return delete_department(id, db)


@router.put("update-department/{id}")
def UpdateDepartment(id : int,department : DepartmentSchemas, db:Session = Depends(get_db)):
    return update_department(id, db, department)