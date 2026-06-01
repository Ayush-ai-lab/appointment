from models.meeting_model import Meeting
from sqlalchemy import or_


def create_meeting(data, db):
    meeting = Meeting(
        name=data.name,
        url=data.url,
        status=data.status,
        created_by=data.created_by,
        updated_by=data.updated_by,
    )
    db.add(meeting)
    db.commit()
    db.refresh(meeting)
    return {"message": "Meeting created successfully", "data": meeting}


def get_all_meeting(db, page: int = 1, limit: int = 12, search: str = None, status: str = None, sort_by: str = "id", sort_order: str = "asc"):
    query = db.query(Meeting)

    if status is not None:
        query = query.filter(Meeting.status == status)

    if search:
        search_term = f"%{search}%"
        query = query.filter(
            or_(
                Meeting.name.ilike(search_term),
                Meeting.url.ilike(search_term),
            )
        )

    total = query.count()
    sort_column = getattr(Meeting, sort_by, Meeting.id)
    if sort_order and sort_order.lower() == "desc":
        query = query.order_by(sort_column.desc())
    else:
        query = query.order_by(sort_column.asc())

    if page < 1:
        page = 1
    if limit < 1:
        limit = 12

    offset = (page - 1) * limit
    meetings = query.offset(offset).limit(limit).all()

    return {
        "message": "Meetings fetched successfully",
        "page": page,
        "limit": limit,
        "total": total,
        "data": meetings,
    }


def get_single_meeting(id, db):
    meeting = db.query(Meeting).filter(Meeting.id == id).first()
    if not meeting:
        return {"message": "No meeting found"}
    return {"message": "Meeting fetch successfully", "data": meeting}


def update_meeting(id, data, db):
    meeting = db.query(Meeting).filter(Meeting.id == id).first()
    if not meeting:
        return {"message": "No meeting found"}

    meeting.name = data.name
    meeting.url = data.url
    meeting.status = data.status
    meeting.updated_by = data.updated_by

    db.commit()
    db.refresh(meeting)
    return {"message": "Meeting update successfully", "data": meeting}


def delete_meeting(id, db):
    meeting = db.query(Meeting).filter(Meeting.id == id).first()
    if not meeting:
        return {"message": "No meeting found"}

    db.delete(meeting)
    db.commit()
    return {"message": "Meeting delete successfully"}
