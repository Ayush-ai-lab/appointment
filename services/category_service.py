from models.category_model import Category


def create_category(data, db):
    category = Category(
        name=data.name,
        department_id=data.department_id,
        slug=data.slug,
        short_description=data.short_description,
        description=data.description,
        status=data.status,
        created_by=data.created_by,
        updated_by=data.updated_by,
    )
    db.add(category)
    db.commit()
    db.refresh(category)
    return {"message": "Category created successfully", "data": category}


def get_all_category(db):
    categories = db.query(Category).all()
    if not categories:
        return {"message": "No category found"}
    return {"message": "Categories fetch successfully", "data": categories}


def get_single_category(id, db):
    category = db.query(Category).filter(Category.id == id).first()
    if not category:
        return {"message": "No category found"}
    return {"message": "Category fetch successfully", "data": category}


def update_category(id, data, db):
    category = db.query(Category).filter(Category.id == id).first()
    if not category:
        return {"message": "No category found"}

    category.name = data.name
    category.department_id = data.department_id
    category.slug = data.slug
    category.short_description = data.short_description
    category.description = data.description
    category.status = data.status
    category.updated_by = data.updated_by

    db.commit()
    db.refresh(category)
    return {"message": "Category update successfully", "data": category}


def delete_category(id, db):
    category = db.query(Category).filter(Category.id == id).first()
    if not category:
        return {"message": "No category found"}

    db.delete(category)
    db.commit()
    return {"message": "Category delete successfully"}
