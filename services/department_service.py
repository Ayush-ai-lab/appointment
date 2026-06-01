from models.department_model import Department
from sqlalchemy import or_


def create_department(data, db):
    department = Department(
        name=data.name,
        slug=data.slug,
        icon=data.icon,
        image=data.image,
        status=data.status,
        created_by=data.created_by,
        updated_by=data.updated_by,
    )
    db.add(department)
    db.commit()
    db.refresh(department)
    return {"message": "Department created successfully", "data": department}


def get_all_department(db, page: int = 1, limit: int = 12, search: str = None, status: str = None, sort_by: str = "id", sort_order: str = "asc"):
    query = db.query(Department)

    if status is not None:
        query = query.filter(Department.status == status)

    if search:
        search_term = f"%{search}%"
        query = query.filter(
            or_(
                Department.name.ilike(search_term),
                Department.slug.ilike(search_term),
            )
        )

    total = query.count()
    sort_column = getattr(Department, sort_by, Department.id)
    if sort_order and sort_order.lower() == "desc":
        query = query.order_by(sort_column.desc())
    else:
        query = query.order_by(sort_column.asc())

    if page < 1:
        page = 1
    if limit < 1:
        limit = 12

    offset = (page - 1) * limit
    departments = query.offset(offset).limit(limit).all()

    return {
        "message": "Departments fetched successfully",
        "page": page,
        "limit": limit,
        "total": total,
        "data": departments,
    }


def get_single_department(id, db):
    department = db.query(Department).filter(Department.id == id).first()
    if not department:
        return {"message": "No department found"}
    return {"message": "Department fetch successfully", "data": department}


def update_department(id, data, db):
    department = db.query(Department).filter(Department.id == id).first()
    if not department:
        return {"message": "No department found"}

    department.name = data.name
    department.slug = data.slug
    department.icon = data.icon
    department.image = data.image
    department.status = data.status
    department.updated_by = data.updated_by

    db.commit()
    db.refresh(department)
    return {"message": "Department update successfully", "data": department}


def delete_department(id, db):
    department = db.query(Department).filter(Department.id == id).first()
    if not department:
        return {"message": "No department found"}

    db.delete(department)
    db.commit()
    return {"message": "Department delete successfully"}
