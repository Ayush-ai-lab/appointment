from models.doctor_model import Doctor


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


def get_all_doctor(db):
    doctors = db.query(Doctor).all()
    if not doctors:
        return {"message": "No doctor found"}
    return {"message": "Doctors fetch successfully", "data": doctors}


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
