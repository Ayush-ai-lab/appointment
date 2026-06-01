from models.meeting_model import Meeting


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


def get_all_meeting(db):
    meetings = db.query(Meeting).all()
    if not meetings:
        return {"message": "No meeting found"}
    return {"message": "Meetings fetch successfully", "data": meetings}


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
