from models.user_model import User


def create_user(data, db):
    user = User(
        name=data.name,
        email=data.email,
        number=data.number,
        password=data.password,
        age=data.age,
        created_by=data.created_by,
        updated_by=data.updated_by,
        status=data.status,
    )
    db.add(user)
    db.commit()
    db.refresh(user)
    return {"message": "User created successfully", "data": user}


def get_all_user(db):
    users = db.query(User).all()
    if not users:
        return {"message": "No user found"}
    return {"message": "Users fetch successfully", "data": users}


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
    user.password = data.password
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
