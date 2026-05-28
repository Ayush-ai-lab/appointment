from models.review_model import Review

def create_review(data,db):

    new_review = Review(
        rating = data.rating,
        message = data.message,
        created_by = data.created_by
    )

    db.add(new_review)
    db.commit()
    db.refresh(new_review)
    return {
        'message': 'Review create successfully',
        'data' : new_review
    }

def get_all_review(db):
    reviews = db.query(Review).all()

    if not reviews :
        return {
            "message" : "No review found"
        }
    
    return {
        "message" : "All review fetch successfully",
        "data" : reviews
    }

def get_single_review(id,db):
    review = db.query(Review).filter(Review.id == id).first()

    if not review:
        return {
            "message" : "No data found"
        }
    
    return {
        "message" : "Review get successfully",
        "data" : review
    }

def update_review(id,data,db):
    review = db.query(Review).filter(Review.id == id).first()

    if not review:
        return {
            "message" : "No review found"
        }
    
    review.rating = data.rating
    review.message = data.message
    
    db.commit()
    db.refresh(review)

    return {
        "message" : "Review update successfully"
    }
    

    
