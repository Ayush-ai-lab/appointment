from fastapi import FastAPI 
from routers.address import routes as address_routes
from core.database import Base, engine
from models.address_model import Address

app = FastAPI()
Base.metadata.create_all(bind=engine)
app.include_router(address_routes)

