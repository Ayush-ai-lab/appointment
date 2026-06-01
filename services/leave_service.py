from models.leave_model import Leave


def create_leave(data, db):
    leave = Leave(
        doctor_id=data.doctor_id,
        specific_date=data.specific_date,
        status=data.status,
        created_by=data.created_by,
        updated_by=data.updated_by,
    )
    db.add(leave)
    db.commit()
    db.refresh(leave)
    return {"message": "Leave created successfully", "data": leave}


def get_all_leave(db):
    leaves = db.query(Leave).all()
    if not leaves:
        return {"message": "No leave found"}
    return {"message": "Leaves fetch successfully", "data": leaves}


def get_single_leave(id, db):
    leave = db.query(Leave).filter(Leave.id == id).first()
    if not leave:
        return {"message": "No leave found"}
    return {"message": "Leave fetch successfully", "data": leave}


def update_leave(id, data, db):
    leave = db.query(Leave).filter(Leave.id == id).first()
    if not leave:
        return {"message": "No leave found"}

    leave.doctor_id = data.doctor_id
    leave.specific_date = data.specific_date
    leave.status = data.status
    leave.updated_by = data.updated_by

    db.commit()
    db.refresh(leave)
    return {"message": "Leave update successfully", "data": leave}


def delete_leave(id, db):
    leave = db.query(Leave).filter(Leave.id == id).first()
    if not leave:
        return {"message": "No leave found"}

    db.delete(leave)
    db.commit()
    return {"message": "Leave delete successfully"}
