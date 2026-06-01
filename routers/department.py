from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from core.database import get_db
from schemas.department import DepartmentSchemas
from services.department_service import create_department, update_department, get_all_department, get_single_department, delete_department

router = APIRouter(prefix="/department", tags=["department"])


@router.post("/create-department")
def CreateDepartment(department: DepartmentSchemas, db: Session = Depends(get_db)):
    return create_department(department, db)


@router.get("/")
def GetDepartments(page: int = 1, limit: int = 12, search: str = None, status: str = None, sort_by: str = "id", sort_order: str = "asc", db: Session = Depends(get_db)):
    return get_all_department(db, page, limit, search, status, sort_by, sort_order)


@router.get("/{id}")
def GetSingleDepartment(id: int, db: Session = Depends(get_db)):
    return get_single_department(id, db)


@router.delete("/delete-department/{id}")
def DeleteDepartment(id: int, db: Session = Depends(get_db)):
    return delete_department(id, db)


@router.put("/update-department/{id}")
def UpdateDepartment(id: int, department: DepartmentSchemas, db: Session = Depends(get_db)):
    return update_department(id, department, db)
