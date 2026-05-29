from models.user_model import User 

def create_user(data, db):
    new_user = User(
        name = data.name,
        email = data.email,
        number = data.number,
        age = data.age,
        password = data.password
    )

    db.add(new_user)
    db.commit()
    db.refresh(new_user)

    return {
        "message": "user update successfully",
        "data": new_user
    }
def get_all_user(db):
    user = db.query(User).all()

    if not user: 
        return {
            "message" : "user not found"
        }
    
    return {
        "message" : "data fetch successfully",
        "data" : user
    }

def get_single_user(id,db):
    user = db.query(User).filter(User.id == id).first()

    if not user: 
        return {
            "message" : "user not found"
        }
    
    return {
        "message" : "data fetch successfully",
        "data" : user
    }

def delete_user(id, db):
    user = db.query(User).filter(User.id == id).first()
    
    if not user:
        return {
            "message" : "No record successfully"
        }
    
    db.delete(user)
    db.commit()

    return {
        "message" : "User delete successfullt"
    }

def update_user(id, data, db):
    user = db.query(User).filter(User.id == id).first()

    if not user:
        return {
            "message" : "No user found"
        }
    
    user.name = data.name 
    user.email = data.email 
    user.number = data.number
    user.password = data.password 
    user.age = data.age 
    
    db.commit()
    db.refresh(user)
    return {
        "message" : "user update successfully"
    }