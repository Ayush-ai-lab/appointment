from models.user_model import User
from core.security import (
    verify_password,
    create_access_token
)
from core.auth import (
    get_current_user,
    admin_required
)

def login_user(data, db):

    user = db.query(User).filter(
        User.email == data.email
    ).first()

    if not user:
        return {"message": "Invalid credentials"}

    if not verify_password(
        data.password,
        user.password
    ):
        return {"message": "Invalid credentials"}

    token = create_access_token(
        {
            "user_id": user.id,
            "email": user.email,
            "role": user.role
        }
    )

    return {
        "access_token": token,
        "token_type": "bearer"
    }


