from models.slot_model import Slot


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


def get_all_slot(db):
    slots = db.query(Slot).all()
    if not slots:
        return {"message": "No slot found"}
    return {"message": "Slots fetch successfully", "data": slots}


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
