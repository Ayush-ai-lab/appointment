from models.availablity_model import DoctorAvailability
from sqlalchemy import or_


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


def get_all_availability(db, page: int = 1, limit: int = 12, search: str = None, status: str = None, doctor_id: int = None, day_of_week: str = None, specific_date: str = None, sort_by: str = "id", sort_order: str = "asc"):
    query = db.query(DoctorAvailability)

    if status is not None:
        query = query.filter(DoctorAvailability.status == status)

    if doctor_id is not None:
        query = query.filter(DoctorAvailability.doctor_id == doctor_id)

    if day_of_week is not None:
        query = query.filter(DoctorAvailability.day_of_week == day_of_week)

    if specific_date is not None:
        query = query.filter(DoctorAvailability.specific_date == specific_date)

    if search:
        search_term = f"%{search}%"
        query = query.filter(
            or_(
                DoctorAvailability.day_of_week.ilike(search_term),
                DoctorAvailability.specific_date.ilike(search_term),
            )
        )

    total = query.count()
    sort_column = getattr(DoctorAvailability, sort_by, DoctorAvailability.id)
    if sort_order and sort_order.lower() == "desc":
        query = query.order_by(sort_column.desc())
    else:
        query = query.order_by(sort_column.asc())

    if page < 1:
        page = 1
    if limit < 1:
        limit = 12

    offset = (page - 1) * limit
    availabilities = query.offset(offset).limit(limit).all()

    return {
        "message": "Availabilities fetched successfully",
        "page": page,
        "limit": limit,
        "total": total,
        "data": availabilities,
    }


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
