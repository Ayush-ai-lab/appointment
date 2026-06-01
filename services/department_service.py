from models.department_model import Department


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


def get_all_department(db):
    departments = db.query(Department).all()
    if not departments:
        return {"message": "No department found"}
    return {"message": "Departments fetch successfully", "data": departments}


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
