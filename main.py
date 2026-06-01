from fastapi import FastAPI 
from core.database import Base, engine
from models.address_model import Address
from models.appointment_model import Appointment
from models.availablity_model import DoctorAvailability
from models.category_model import Category
from models.department_model import Department
from models.doctor_model import Doctor
from models.faq_model import Faq
from models.leave_model import Leave
from models.meeting_model import Meeting
from models.patient_history import PatientHistory
from models.review_model import Review
from models.slot_model import Slot
from models.user_model import User
from routers.address import routes as address_routes
from routers.appointment import router as appointment_router
from routers.availablity import router as availability_router
from routers.category import router as category_router
from routers.department import router as department_router
from routers.doctor import router as doctor_router
from routers.faq import router as faq_router
from routers.leave import router as leave_router
from routers.meeting import router as meeting_router
from routers.patient import router as patient_router
from routers.review import router as review_router
from routers.slot import router as slot_router
from routers.user import router as user_router

app = FastAPI()
Base.metadata.create_all(bind=engine)
app.include_router(address_routes)
app.include_router(appointment_router)
app.include_router(availability_router)
app.include_router(category_router)
app.include_router(department_router)
app.include_router(doctor_router)
app.include_router(faq_router)
app.include_router(leave_router)
app.include_router(meeting_router)
app.include_router(patient_router)
app.include_router(review_router)
app.include_router(slot_router)
app.include_router(user_router)

