from typing import Optional, List
from beanie import Document, Link
from pydantic import BaseModel, EmailStr
from models.events import Event

class User(Document):
    email: EmailStr
    password: str
    events: Optional[List[Event]]
  
    class Settings:
        name = "users"
  
    class Config:
        schema_extra = {
            "example": {
                "email": "fastapi@packt.com",
                "username": "strong!!!",
                "events": [],
            }
        }
  
class UserSignIn(Document):
    email: EmailStr
    password: str
