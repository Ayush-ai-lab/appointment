from models.address_model import Address


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


def get_all_address(db):
    addresses = db.query(Address).all()
    if not addresses:
        return {"message": "No address found"}
    return {"message": "Addresses fetch successfully", "data": addresses}


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
