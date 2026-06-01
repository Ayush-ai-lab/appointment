from models.category_model import Category
from sqlalchemy import or_


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


def get_all_category(db, page: int = 1, limit: int = 12, search: str = None, status: str = None, department_id: int = None, sort_by: str = "id", sort_order: str = "asc"):
    query = db.query(Category)

    if status is not None:
        query = query.filter(Category.status == status)

    if department_id is not None:
        query = query.filter(Category.department_id == department_id)

    if search:
        search_term = f"%{search}%"
        query = query.filter(
            or_(
                Category.name.ilike(search_term),
                Category.slug.ilike(search_term),
                Category.short_description.ilike(search_term),
                Category.description.ilike(search_term),
            )
        )

    total = query.count()
    sort_column = getattr(Category, sort_by, Category.id)
    if sort_order and sort_order.lower() == "desc":
        query = query.order_by(sort_column.desc())
    else:
        query = query.order_by(sort_column.asc())

    if page < 1:
        page = 1
    if limit < 1:
        limit = 12

    offset = (page - 1) * limit
    categories = query.offset(offset).limit(limit).all()

    return {
        "message": "Categories fetched successfully",
        "page": page,
        "limit": limit,
        "total": total,
        "data": categories,
    }


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
