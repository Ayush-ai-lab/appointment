from models.address_model import Address
from sqlalchemy import or_


def Add_address(data, db):
    address = Address(
        country=data.country,
        state=data.state,
        city=data.city,
        street_address=data.street_address,
        address=data.address,
        pin_code=data.pin_code,
        user_id=data.user_id,
        created_by=data.created_by,
        updated_by=data.updated_by,
        status=data.status,
    )
    db.add(address)
    db.commit()
    db.refresh(address)
    return {"message": "Address created successfully", "data": address}


def get_all_address(db, page: int = 1, limit: int = 12, search: str = None, status: str = None, user_id: int = None, sort_by: str = "id", sort_order: str = "asc"):
    query = db.query(Address)

    if status is not None:
        query = query.filter(Address.status == status)

    if user_id is not None:
        query = query.filter(Address.user_id == user_id)

    if search:
        search_term = f"%{search}%"
        query = query.filter(
            or_(
                Address.country.ilike(search_term),
                Address.state.ilike(search_term),
                Address.city.ilike(search_term),
                Address.street_address.ilike(search_term),
                Address.address.ilike(search_term),
            )
        )

    total = query.count()
    sort_column = getattr(Address, sort_by, Address.id)
    if sort_order and sort_order.lower() == "desc":
        query = query.order_by(sort_column.desc())
    else:
        query = query.order_by(sort_column.asc())

    if page < 1:
        page = 1
    if limit < 1:
        limit = 12

    offset = (page - 1) * limit
    addresses = query.offset(offset).limit(limit).all()

    return {
        "message": "Addresses fetched successfully",
        "page": page,
        "limit": limit,
        "total": total,
        "data": addresses,
    }


def get_single_address(id, db):
    address = db.query(Address).filter(Address.id == id).first()
    if not address:
        return {"message": "No address found"}
    return {"message": "Address fetch successfully", "data": address}


def update_address(id, data, db):
    address = db.query(Address).filter(Address.id == id).first()
    if not address:
        return {"message": "No address found"}

    address.country = data.country
    address.state = data.state
    address.city = data.city
    address.street_address = data.street_address
    address.address = data.address
    address.pin_code = data.pin_code
    address.user_id = data.user_id
    address.updated_by = data.updated_by
    address.status = data.status

    db.commit()
    db.refresh(address)
    return {"message": "Address update successfully", "data": address}


def delete_address(id, db):
    address = db.query(Address).filter(Address.id == id).first()
    if not address:
        return {"message": "No address found"}

    db.delete(address)
    db.commit()
    return {"message": "Address delete successfully"}
