from pydantic import BaseModel
from datetime import datetime

class UserBase(BaseModel):
    email: str

class UserOut(UserBase):
    id: int
    created_at: datetime

    class Config:
        orm_mode = True
