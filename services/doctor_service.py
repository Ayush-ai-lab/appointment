from models.doctor_model import Doctor
from sqlalchemy import or_


def create_doctor(data, db):
    doctor = Doctor(
        name=data.name,
        email=data.email,
        number=data.number,
        experience=data.experience,
        qualification=data.qualification,
        bio=data.bio,
        category_id=data.category_id,
        status=data.status,
        created_by=data.created_by,
        updated_by=data.updated_by,
    )
    db.add(doctor)
    db.commit()
    db.refresh(doctor)
    return {"message": "Doctor created successfully", "data": doctor}


def get_all_doctor(db, page: int = 1, limit: int = 12, search: str = None, status: str = None, category_id: int = None, sort_by: str = "id", sort_order: str = "asc"):
    query = db.query(Doctor)

    if status is not None:
        query = query.filter(Doctor.status == status)

    if category_id is not None:
        query = query.filter(Doctor.category_id == category_id)

    if search:
        search_term = f"%{search}%"
        query = query.filter(
            or_(
                Doctor.name.ilike(search_term),
                Doctor.email.ilike(search_term),
                Doctor.qualification.ilike(search_term),
                Doctor.bio.ilike(search_term),
            )
        )

    total = query.count()
    sort_column = getattr(Doctor, sort_by, Doctor.id)
    if sort_order and sort_order.lower() == "desc":
        query = query.order_by(sort_column.desc())
    else:
        query = query.order_by(sort_column.asc())

    if page < 1:
        page = 1
    if limit < 1:
        limit = 12

    offset = (page - 1) * limit
    doctors = query.offset(offset).limit(limit).all()

    return {
        "message": "Doctors fetched successfully",
        "page": page,
        "limit": limit,
        "total": total,
        "data": doctors,
    }


def get_single_doctor(id, db):
    doctor = db.query(Doctor).filter(Doctor.id == id).first()
    if not doctor:
        return {"message": "No doctor found"}
    return {"message": "Doctor fetch successfully", "data": doctor}


def update_doctor(id, data, db):
    doctor = db.query(Doctor).filter(Doctor.id == id).first()
    if not doctor:
        return {"message": "No doctor found"}

    doctor.name = data.name
    doctor.email = data.email
    doctor.number = data.number
    doctor.experience = data.experience
    doctor.qualification = data.qualification
    doctor.bio = data.bio
    doctor.category_id = data.category_id
    doctor.status = data.status
    doctor.updated_by = data.updated_by

    db.commit()
    db.refresh(doctor)
    return {"message": "Doctor update successfully", "data": doctor}


def delete_doctor(id, db):
    doctor = db.query(Doctor).filter(Doctor.id == id).first()
    if not doctor:
        return {"message": "No doctor found"}

    db.delete(doctor)
    db.commit()
    return {"message": "Doctor delete successfully"}
