from models.department_model import Department 

def create_department(db, department):
    new_department = Department(
        name = department.name,
        slug = department.slug,
        icon = department.icon,
        image = department.image,
        status = department.status,
        created_by = department.created_by

    )
    
    db.add(new_department)
    db.commit()
    db.refresh(new_department)

    return {
        "message" : "Department created successfully",
        "data": new_department
    }

def get_all_department(db):
    departments = db.query(Department).all()

    if not departments :
        return {
            "message" : "No departments found"
        }
    
    return {
        "message" : "Departments found successfully",
        "data": departments
    }

def get_single_department(id,db):
    department = db.query(Department).filter(Department.id == id).first()

    if not department:
        return {
            "message" : "Department not found",
        } 
    
    return {
        "message": "department found successfully",
        "data": department
    }


def delete_department(id,db):
    department = db.query(Department).filter(Department.id == id).first()

    if not department :
        return {
            "message" : "Department not found", 
        }

    db.delete(department)
    db.commit()

    return {
        "message" : "department deleted successfully",
        
    }

def update_department(id, db, department):
    old_department = db.query(Department).filter(Department.id == id).first()

    if not old_department:
        return {
            "message" : "Department not found", 
        }
    
    old_department.name = department.name
    old_department.slug = department.slug
    old_department.icon = department.icon
    old_department.image = department.image
    old_department.status = department.status
    old_department.created_by = department.created_by

    db.commit()
    db.refresh(old_department)

    return {
        "message" : "Department updated successfully",
        "data": old_department
    }