from models.slot_model import Slot
from sqlalchemy import or_


def create_slot(data, db):
    slot = Slot(
        status=data.status,
        doctor_id=data.doctor_id,
        slot_start=data.slot_start,
        slot_end=data.slot_end,
        slot_date=data.slot_date,
        created_by=data.created_by,
        updated_by=data.updated_by,
    )
    db.add(slot)
    db.commit()
    db.refresh(slot)
    return {"message": "Slot created successfully", "data": slot}


def get_all_slot(db, page: int = 1, limit: int = 12, search: str = None, status: str = None, doctor_id: int = None, slot_date: str = None, sort_by: str = "id", sort_order: str = "asc"):
    query = db.query(Slot)

    if status is not None:
        query = query.filter(Slot.status == status)

    if doctor_id is not None:
        query = query.filter(Slot.doctor_id == doctor_id)

    if slot_date is not None:
        query = query.filter(Slot.slot_date == slot_date)

    if search:
        search_term = f"%{search}%"
        query = query.filter(Slot.slot_date.ilike(search_term))

    total = query.count()
    sort_column = getattr(Slot, sort_by, Slot.id)
    if sort_order and sort_order.lower() == "desc":
        query = query.order_by(sort_column.desc())
    else:
        query = query.order_by(sort_column.asc())

    if page < 1:
        page = 1
    if limit < 1:
        limit = 12

    offset = (page - 1) * limit
    slots = query.offset(offset).limit(limit).all()

    return {
        "message": "Slots fetched successfully",
        "page": page,
        "limit": limit,
        "total": total,
        "data": slots,
    }


def get_single_slot(id, db):
    slot = db.query(Slot).filter(Slot.id == id).first()
    if not slot:
        return {"message": "No slot found"}
    return {"message": "Slot fetch successfully", "data": slot}


def update_slot(id, data, db):
    slot = db.query(Slot).filter(Slot.id == id).first()
    if not slot:
        return {"message": "No slot found"}

    slot.status = data.status
    slot.doctor_id = data.doctor_id
    slot.slot_start = data.slot_start
    slot.slot_end = data.slot_end
    slot.slot_date = data.slot_date
    slot.updated_by = data.updated_by

    db.commit()
    db.refresh(slot)
    return {"message": "Slot update successfully", "data": slot}


def delete_slot(id, db):
    slot = db.query(Slot).filter(Slot.id == id).first()
    if not slot:
        return {"message": "No slot found"}

    db.delete(slot)
    db.commit()
    return {"message": "Slot delete successfully"}
