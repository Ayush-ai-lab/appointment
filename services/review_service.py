from models.review_model import Review
from sqlalchemy import or_


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


def get_all_review(db, page: int = 1, limit: int = 12, search: str = None, status: str = None, rating: int = None, sort_by: str = "id", sort_order: str = "asc"):
    query = db.query(Review)

    if status is not None:
        query = query.filter(Review.status == status)

    if rating is not None:
        query = query.filter(Review.rating == rating)

    if search:
        search_term = f"%{search}%"
        query = query.filter(Review.message.ilike(search_term))

    total = query.count()
    sort_column = getattr(Review, sort_by, Review.id)
    if sort_order and sort_order.lower() == "desc":
        query = query.order_by(sort_column.desc())
    else:
        query = query.order_by(sort_column.asc())

    if page < 1:
        page = 1
    if limit < 1:
        limit = 12

    offset = (page - 1) * limit
    reviews = query.offset(offset).limit(limit).all()

    return {
        "message": "Reviews fetched successfully",
        "page": page,
        "limit": limit,
        "total": total,
        "data": reviews,
    }


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
