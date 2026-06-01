from models.faq_model import Faq
from sqlalchemy import or_


def create_faq(data, db):
    faq = Faq(
        question=data.question,
        answer=data.answer,
        status=data.status,
        created_by=data.created_by,
        updated_by=data.updated_by,
    )
    db.add(faq)
    db.commit()
    db.refresh(faq)
    return {"message": "Faq created successfully", "data": faq}


def get_all_faq(db, page: int = 1, limit: int = 12, search: str = None, status: str = None, sort_by: str = "id", sort_order: str = "asc"):
    query = db.query(Faq)

    if status is not None:
        query = query.filter(Faq.status == status)

    if search:
        search_term = f"%{search}%"
        query = query.filter(
            or_(
                Faq.question.ilike(search_term),
                Faq.answer.ilike(search_term),
            )
        )

    total = query.count()
    sort_column = getattr(Faq, sort_by, Faq.id)
    if sort_order and sort_order.lower() == "desc":
        query = query.order_by(sort_column.desc())
    else:
        query = query.order_by(sort_column.asc())

    if page < 1:
        page = 1
    if limit < 1:
        limit = 12

    offset = (page - 1) * limit
    faqs = query.offset(offset).limit(limit).all()

    return {
        "message": "Faqs fetched successfully",
        "page": page,
        "limit": limit,
        "total": total,
        "data": faqs,
    }


def get_single_faq(id, db):
    faq = db.query(Faq).filter(Faq.id == id).first()
    if not faq:
        return {"message": "No faq found"}
    return {"message": "Faq fetch successfully", "data": faq}


def update_faq(id, data, db):
    faq = db.query(Faq).filter(Faq.id == id).first()
    if not faq:
        return {"message": "No faq found"}

    faq.question = data.question
    faq.answer = data.answer
    faq.status = data.status
    faq.updated_by = data.updated_by

    db.commit()
    db.refresh(faq)
    return {"message": "Faq update successfully", "data": faq}


def delete_faq(id, db):
    faq = db.query(Faq).filter(Faq.id == id).first()
    if not faq:
        return {"message": "No faq found"}

    db.delete(faq)
    db.commit()
    return {"message": "Faq delete successfully"}
