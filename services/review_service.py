from models.review_model import Review


def create_review(data, db):
    review = Review(
        rating=data.rating,
        message=data.message,
        created_by=data.created_by,
        updated_by=data.updated_by,
        status=data.status,
    )
    db.add(review)
    db.commit()
    db.refresh(review)
    return {"message": "Review created successfully", "data": review}


def get_all_review(db):
    reviews = db.query(Review).all()
    if not reviews:
        return {"message": "No review found"}
    return {"message": "Reviews fetch successfully", "data": reviews}


def get_single_review(id, db):
    review = db.query(Review).filter(Review.id == id).first()
    if not review:
        return {"message": "No review found"}
    return {"message": "Review fetch successfully", "data": review}


def update_review(id, data, db):
    review = db.query(Review).filter(Review.id == id).first()
    if not review:
        return {"message": "No review found"}

    review.rating = data.rating
    review.message = data.message
    review.updated_by = data.updated_by
    review.status = data.status

    db.commit()
    db.refresh(review)
    return {"message": "Review update successfully", "data": review}


def delete_review(id, db):
    review = db.query(Review).filter(Review.id == id).first()
    if not review:
        return {"message": "No review found"}

    db.delete(review)
    db.commit()
    return {"message": "Review delete successfully"}
