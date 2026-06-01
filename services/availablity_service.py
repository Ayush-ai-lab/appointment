from models.availablity_model import DoctorAvailability


def create_availability(data, db):
    availability = DoctorAvailability(
        status=data.status,
        doctor_id=data.doctor_id,
        day_of_week=data.day_of_week,
        start_time=data.start_time,
        end_time=data.end_time,
        slot_interval=data.slot_interval,
        break_start=data.break_start,
        break_end=data.break_end,
        leave_id=data.leave_id,
        specific_date=data.specific_date,
        created_by=data.created_by,
        updated_by=data.updated_by,
    )
    db.add(availability)
    db.commit()
    db.refresh(availability)
    return {"message": "Availability created successfully", "data": availability}


def get_all_availability(db):
    availabilities = db.query(DoctorAvailability).all()
    if not availabilities:
        return {"message": "No availability found"}
    return {"message": "Availabilities fetch successfully", "data": availabilities}


def get_single_availability(id, db):
    availability = db.query(DoctorAvailability).filter(DoctorAvailability.id == id).first()
    if not availability:
        return {"message": "No availability found"}
    return {"message": "Availability fetch successfully", "data": availability}


def update_availability(id, data, db):
    availability = db.query(DoctorAvailability).filter(DoctorAvailability.id == id).first()
    if not availability:
        return {"message": "No availability found"}

    availability.status = data.status
    availability.doctor_id = data.doctor_id
    availability.day_of_week = data.day_of_week
    availability.start_time = data.start_time
    availability.end_time = data.end_time
    availability.slot_interval = data.slot_interval
    availability.break_start = data.break_start
    availability.break_end = data.break_end
    availability.leave_id = data.leave_id
    availability.specific_date = data.specific_date
    availability.updated_by = data.updated_by

    db.commit()
    db.refresh(availability)
    return {"message": "Availability update successfully", "data": availability}


def delete_availability(id, db):
    availability = db.query(DoctorAvailability).filter(DoctorAvailability.id == id).first()
    if not availability:
        return {"message": "No availability found"}

    db.delete(availability)
    db.commit()
    return {"message": "Availability delete successfully"}
