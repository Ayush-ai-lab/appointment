from models.user_model import User
from sqlalchemy import or_
from core.security import hash_password

def create_user(data, db):
    user = User(
        name=data.name,
        email=data.email,
        number=data.number,
        password=hash_password(data.password),
        age=data.age,
        created_by=data.created_by,
        updated_by=data.updated_by,
        status=data.status,
    )
    db.add(user)
    db.commit()
    db.refresh(user)
    return {"message": "User created successfully", "data": user}


def get_all_user(db, page: int = 1, limit: int = 12, search: str = None, status: str = None, sort_by: str = "id", sort_order: str = "asc"):
    query = db.query(User)

    if status is not None:
        query = query.filter(User.status == status)

    if search:
        search_term = f"%{search}%"
        query = query.filter(
            or_(
                User.name.ilike(search_term),
                User.email.ilike(search_term),
            )
        )

    total = query.count()
    sort_column = getattr(User, sort_by, User.id)
    if sort_order and sort_order.lower() == "desc":
        query = query.order_by(sort_column.desc())
    else:
        query = query.order_by(sort_column.asc())

    if page < 1:
        page = 1
    if limit < 1:
        limit = 12

    offset = (page - 1) * limit
    users = query.offset(offset).limit(limit).all()

    return {
        "message": "Users fetched successfully",
        "page": page,
        "limit": limit,
        "total": total,
        "data": users,
    }


def get_single_user(id, db):
    user = db.query(User).filter(User.id == id).first()
    if not user:
        return {"message": "No user found"}
    return {"message": "User fetch successfully", "data": user}


def update_user(id, data, db):
    user = db.query(User).filter(User.id == id).first()
    if not user:
        return {"message": "No user found"}

    user.name = data.name
    user.email = data.email
    user.number = data.number
    user.password = hash_password(data.password),
    user.age = data.age
    user.updated_by = data.updated_by
    user.status = data.status

    db.commit()
    db.refresh(user)
    return {"message": "User update successfully", "data": user}


def delete_user(id, db):
    user = db.query(User).filter(User.id == id).first()
    if not user:
        return {"message": "No user found"}

    db.delete(user)
    db.commit()
    return {"message": "User delete successfully"}
