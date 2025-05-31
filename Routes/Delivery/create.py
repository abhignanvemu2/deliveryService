from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from Schemas.DeliveryPerson import createDeliveryPersonInterface
from Models.DeliveryAgent import DeliveryAgent
from Config import get_db

router = APIRouter()

@router.post('/')
def createDeliveryPerson (data: createDeliveryPersonInterface, db: Session =Depends (get_db) ) :
    try:
      deliveryPerson = DeliveryAgent(
         name = data.name,
         email = data.email,
         phone = data.phone,
         is_available = 1
      )
      db.add(deliveryPerson)
      db.commit()
      db.refresh(deliveryPerson)

      return{
         "name" : deliveryPerson.name,
         "email"  : deliveryPerson.email,
         "phone" : deliveryPerson.phone

      }

    except Exception as e:
       db.rollback()
       raise HTTPException(status_code=500, detail=f"Error creating new delivery agent: {str(e)}")
    

