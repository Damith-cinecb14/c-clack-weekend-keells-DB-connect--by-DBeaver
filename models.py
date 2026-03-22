from datetime import datetime

from pydantic import BaseModel


class UserCreate(BaseModel):
    name:str
    email:str

class UserResponse(BaseModel):
    id:int
    name:str
    email:str


class InvoiceCreate(BaseModel):
    user_id:int
    amount:float
    description:str

class InvoiceResponse(BaseModel):
    id:int
    user_id: int
    amount:float
    description:str
    created_at:datetime