from models.category_model import Category

def create_category(data,db):
    new_category = Category(
        name = data.name,
        short_description = data.short_description,
        description = data.description,
        status = data.status
        create_by = data.create_by
    )

    db.add(new_category)
    db.commit()
    db.refresh(new_category)

    return {
        "message": "Category created successfully"
    }

def get_all_category(db):
    category = db.query(Category).all()

    if not category:
        return {
            "message": "No category found"
        }
    
    return {
        "message" : "Category fetch successfully",
        "data" : category
    }

def get_single_category(id,db):
    category = db.query(Category).filter(Category.id == id).first()

    if not category:
        return {
            "message": "No category found"
        }
    
    return {
        "message" : "Category fetch successfully",
        "data" : category
    }

def delete_category(id,db):
    category = db.query(Category).filter(Category.id == id).first()

    if not category:
        return {
            "message": "No category found"
        }
    
    db.delete(category)
    db.commit()

    return {
        "message": "record delete successfully"
    }


def update_category(id,data,db):
    old_category = db.query(Category).filter(Category.id == id).first()

    if not old_category:
        return {
            "message": "No category found"
        }
    
    old_category.name = data.name
    old_category.short_description = data.short_description
    old_category.description = data.description
    old_category.status = data.status

    db.commit()
    db.refresh(old_category)
    return {
        "message": "Category update successfully",
        
    }