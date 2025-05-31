from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from Models.DeliveryAgent import DeliveryAgent
from Config import get_db  # Ensure this points to the actual `get_db` in your db config

router = APIRouter()

@router.get('/available')
def get_available_agents(db: Session = Depends(get_db)):
    delivery_people = db.query(DeliveryAgent).filter(DeliveryAgent.is_available == 1).all()

    if not delivery_people:
        raise HTTPException(status_code=404, detail="All delivery agents are currently busy")

    return delivery_people
