from models.patient_history import PatientHistory


def create_patient_history(data, db):
    patient_history = PatientHistory(
        user_id=data.user_id,
        email=data.email,
        mobile_number=data.mobile_number,
        registration_number=data.registration_number,
        doctor_id=data.doctor_id,
        appointment_id=data.appointment_id,
        symptoms=data.symptoms,
        diagnosis=data.diagnosis,
        prescription=data.prescription,
        created_by=data.created_by,
        updated_by=data.updated_by,
        status=data.status,
    )
    db.add(patient_history)
    db.commit()
    db.refresh(patient_history)
    return {"message": "Patient history created successfully", "data": patient_history}


def get_all_patient_history(db):
    patient_histories = db.query(PatientHistory).all()
    if not patient_histories:
        return {"message": "No patient history found"}
    return {"message": "Patient histories fetch successfully", "data": patient_histories}


def get_single_patient_history(id, db):
    patient_history = db.query(PatientHistory).filter(PatientHistory.id == id).first()
    if not patient_history:
        return {"message": "No patient history found"}
    return {"message": "Patient history fetch successfully", "data": patient_history}


def update_patient_history(id, data, db):
    patient_history = db.query(PatientHistory).filter(PatientHistory.id == id).first()
    if not patient_history:
        return {"message": "No patient history found"}

    patient_history.user_id = data.user_id
    patient_history.email = data.email
    patient_history.mobile_number = data.mobile_number
    patient_history.registration_number = data.registration_number
    patient_history.doctor_id = data.doctor_id
    patient_history.appointment_id = data.appointment_id
    patient_history.symptoms = data.symptoms
    patient_history.diagnosis = data.diagnosis
    patient_history.prescription = data.prescription
    patient_history.updated_by = data.updated_by
    patient_history.status = data.status

    db.commit()
    db.refresh(patient_history)
    return {"message": "Patient history update successfully", "data": patient_history}


def delete_patient_history(id, db):
    patient_history = db.query(PatientHistory).filter(PatientHistory.id == id).first()
    if not patient_history:
        return {"message": "No patient history found"}

    db.delete(patient_history)
    db.commit()
    return {"message": "Patient history delete successfully"}
