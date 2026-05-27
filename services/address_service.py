from models.address_model import Address

def Add_address(address, db):
    address = Address(
        country = address.country,
        state = address.state,
        city = address.city,
        address = address.address,
        street_address = address.street_address,
        pin_code = address.pin_code
    )

    db.add(address)
    db.commit()
    db.refresh(address)
    return {
        "message": "Address Added Successfully",
        "data": address
    }

def UpdateAddress(id, address, db):
    old_address = db.query(Address).filter(Address.id == id).first()

    if not old_address:
        return {
            "message" : "No address found"
        }
    

    old_address.country = address.country
    old_address.state = address.state
    old_address.city = address.city
    old_address.street_address = address.street_address
    old_address.address = address.address
    old_address.pin_code = address.pin_code

    db.commit()
    db.refresh(old_address)
    return {
        "message" : "address update successfully"
    }

def get_all_address(db):
    addresses = db.query(Address).all()
    if not addresses:
        return {
            "message" : "No address found"
        }
    return {
        "message": "All record get successfully",
        "data" : addresses
    }

def get_single_address(id,db):
    address = db.query(Address).filter(Address.id == id).first()
    if not address:
        return {
            "message" : "No address found"
        }
    return {
        "message": "Record get successfully",
        "data" : address
    }

def delete_address(id,db):
    address = db.query(Address).filter(Address.id == id).first()

    if not address:
        return {
            "message" : "No address found"
        }
    
    db.delete(address)
    db.commit()
  
    return {
        "message" : "Address delete successfully"
    }