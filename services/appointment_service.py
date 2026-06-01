from models.appointment_model import Appointment
from sqlalchemy import or_


def create_appointment(data, db):
    appointment = Appointment(
        status=data.status,
        department_id=data.department_id,
        user_id=data.user_id,
        category_id=data.category_id,
        short_description=data.short_description,
        appointment_date=data.appointment_date,
        appointment_status=data.appointment_status,
        payment_status=data.payment_status,
        notes=data.notes,
        symptoms=data.symptoms,
        doctor_id=data.doctor_id,
        slot_id=data.slot_id,
        appointment_valid_date=data.appointment_valid_date,
        prescription=data.prescription,
        meeting_id=data.meeting_id,
        weight=data.weight,
        bp=data.bp,
        created_by=data.created_by,
        updated_by=data.updated_by,
    )
    db.add(appointment)
    db.commit()
    db.refresh(appointment)
    return {"message": "Appointment created successfully", "data": appointment}


def get_all_appointment(db, page: int = 1, limit: int = 12, search: str = None, status: str = None, payment_status: int = None, department_id: int = None, user_id: int = None, category_id: int = None, doctor_id: int = None, slot_id: int = None, sort_by: str = "id", sort_order: str = "asc"):
    query = db.query(Appointment)

    if status is not None:
        query = query.filter(Appointment.status == status)

    if payment_status is not None:
        query = query.filter(Appointment.payment_status == payment_status)

    if department_id is not None:
        query = query.filter(Appointment.department_id == department_id)

    if user_id is not None:
        query = query.filter(Appointment.user_id == user_id)

    if category_id is not None:
        query = query.filter(Appointment.category_id == category_id)

    if doctor_id is not None:
        query = query.filter(Appointment.doctor_id == doctor_id)

    if slot_id is not None:
        query = query.filter(Appointment.slot_id == slot_id)

    if search:
        search_term = f"%{search}%"
        query = query.filter(
            or_(
                Appointment.short_description.ilike(search_term),
                Appointment.notes.ilike(search_term),
                Appointment.symptoms.ilike(search_term),
            )
        )

    total = query.count()
    sort_column = getattr(Appointment, sort_by, Appointment.id)
    if sort_order and sort_order.lower() == "desc":
        query = query.order_by(sort_column.desc())
    else:
        query = query.order_by(sort_column.asc())

    if page < 1:
        page = 1
    if limit < 1:
        limit = 12

    offset = (page - 1) * limit
    appointment = query.offset(offset).limit(limit).all()

    return {
        "message": "Appointments fetched successfully",
        "page": page,
        "limit": limit,
        "total": total,
        "data": appointment,
    }


def get_single_appointment(id, db):
    appointment = db.query(Appointment).filter(Appointment.id == id).first()
    if not appointment:
        return {"message": "No appointment found"}
    return {"message": "Appointment fetch successfully", "data": appointment}


def update_appointment(id, data, db):
    appointment = db.query(Appointment).filter(Appointment.id == id).first()
    if not appointment:
        return {"message": "No appointment found"}

    appointment.status = data.status
    appointment.department_id = data.department_id
    appointment.user_id = data.user_id
    appointment.category_id = data.category_id
    appointment.short_description = data.short_description
    appointment.appointment_date = data.appointment_date
    appointment.appointment_status = data.appointment_status
    appointment.payment_status = data.payment_status
    appointment.notes = data.notes
    appointment.symptoms = data.symptoms
    appointment.doctor_id = data.doctor_id
    appointment.slot_id = data.slot_id
    appointment.appointment_valid_date = data.appointment_valid_date
    appointment.prescription = data.prescription
    appointment.meeting_id = data.meeting_id
    appointment.weight = data.weight
    appointment.bp = data.bp
    appointment.updated_by = data.updated_by

    db.commit()
    db.refresh(appointment)
    return {"message": "Appointment update successfully", "data": appointment}


def delete_appointment(id, db):
    appointment = db.query(Appointment).filter(Appointment.id == id).first()
    if not appointment:
        return {"message": "No appointment found"}

    db.delete(appointment)
    db.commit()
    return {"message": "Appointment delete successfully"}
