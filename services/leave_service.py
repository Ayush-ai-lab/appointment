from models.leave_model import Leave
from sqlalchemy import or_


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


def get_all_leave(db, page: int = 1, limit: int = 12, search: str = None, status: str = None, doctor_id: int = None, specific_date: str = None, sort_by: str = "id", sort_order: str = "asc"):
    query = db.query(Leave)

    if status is not None:
        query = query.filter(Leave.status == status)

    if doctor_id is not None:
        query = query.filter(Leave.doctor_id == doctor_id)

    if specific_date is not None:
        query = query.filter(Leave.specific_date == specific_date)

    if search:
        search_term = f"%{search}%"
        query = query.filter(Leave.specific_date.ilike(search_term))

    total = query.count()
    sort_column = getattr(Leave, sort_by, Leave.id)
    if sort_order and sort_order.lower() == "desc":
        query = query.order_by(sort_column.desc())
    else:
        query = query.order_by(sort_column.asc())

    if page < 1:
        page = 1
    if limit < 1:
        limit = 12

    offset = (page - 1) * limit
    leaves = query.offset(offset).limit(limit).all()

    return {
        "message": "Leaves fetched successfully",
        "page": page,
        "limit": limit,
        "total": total,
        "data": leaves,
    }


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
