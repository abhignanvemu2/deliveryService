from pydantic import BaseModel, constr, EmailStr

class createDeliveryPersonInterface(BaseModel):
    name: str = constr(strip_whitespace=True, min_length=1) 
    email: str = constr(strip_whitespace=True, min_length=1) 
    phone: str = constr(strip_whitespace=True, min_length=1) 

class updateStatus(BaseModel) :
    status : int