from models.doctor_model import Doctor 

def create_doctor(data, db):
    new_doctor = Doctor(
        name = data.name ,
        email = data.email,
        number = data.number,
        experience = data.experience,
        qualification = data.qualification,
        bio = data.bio,
        created_by = data.created_by,
        updated_by = data.updated_by
    ) 

    db.add(new_doctor)
    db.commit()
    db.refresh(new_doctor)

    return {
        "message" : "Doctor created successfully",
        "data" : new_doctor
    }

def get_all_doctor(db):
    doctors = db.query(Doctor).all()

    if not doctors:
        return {
            "message" : "no doctor found"
        }
    
    return {
        "message" : "record fetch successfully",
        "data" : doctors
    }

def get_single_doctor(id,db):
    doctor = db.query(Doctor).filter(Doctor.id == id).first()
    
    if not doctor:
        return {
            "message" : "no record found"
        }
    
    return {
        "message" : "record fetch successfully",
        "data" : doctor
    }


def update_doctor(id,data,db):
    doctor = db.query(Doctor).filter(Doctor.id == id).first()

    if not doctor:
        return {
            "message" : "no record found"
        }
    
    doctor.name = data.name
    doctor.email = data.email
    doctor.number = data.number
    doctor.experience = data.experience
    doctor.qualification = data.qualification
    doctor.bio = data.bio
    doctor.updated_by = data.updated_by

    db.commit()
    db.refresh(doctor)

    return {
        "message" : "record updated successfully",
        "data" : doctor
    }

def delete_doctor(id,db):
    doctor = db.query(Doctor).filter(Doctor.id == id).first()

    if not doctor:
        return {
            "message" : "no record found"
        }
    
    db.delete(doctor)
    db.commit()

    return {
        "message" : "record deleted successfully"
    }