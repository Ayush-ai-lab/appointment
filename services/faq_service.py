from models.faq_model import Faq


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


def get_all_faq(db):
    faqs = db.query(Faq).all()
    if not faqs:
        return {"message": "No faq found"}
    return {"message": "Faqs fetch successfully", "data": faqs}


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
