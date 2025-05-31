from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from Models.DeliveryAgent import DeliveryAgent
from Config import get_db
from Models.OrderModel import Order
from Schemas.DeliveryPerson import updateStatus
from sqlalchemy.exc import SQLAlchemyError

router = APIRouter()

@router.patch('/{orderId}/delivery/{deliveryAgentId}')
def update_delivery_status(
    orderId: int,
    deliveryAgentId: int,
    data: updateStatus,
    db: Session = Depends(get_db)
):
    try:
        order = db.get(Order, orderId)
        agent = db.get(DeliveryAgent, deliveryAgentId)
        if order is None:
            raise HTTPException(status_code=404, detail="No Order Found")
        
        if order.delivery_agent_id != deliveryAgentId:
            raise HTTPException(status_code=403, detail="You are not the delivery agent for this order")
        
        if data.status == 3 :
            order.status = 4
            agent.is_available = 1

        
        # Update delivery status
        order.delivery_status = data.status
        db.commit()
        db.refresh(order)

        return order

    except SQLAlchemyError as e:
        db.rollback()
        raise HTTPException(status_code=500, detail=f"Database error: {str(e)}")

    except Exception as e:
        db.rollback()
        raise HTTPException(status_code=500, detail=f"Unexpected error: {str(e)}")
