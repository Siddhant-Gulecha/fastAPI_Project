# schemas.py
from pydantic import BaseModel, EmailStr
from typing import List, Optional


# ----- User Schemas -----
class UserCreateRequest(BaseModel):
    name: str
    email: EmailStr
    age: int


class UserUpdateRequest(BaseModel):
    name: Optional[str]
    email: Optional[EmailStr]
    age: Optional[int]

class UserResponse(BaseModel):
    id: int
    name: str
    email: EmailStr
    age: int
    class Config:
        orm_mode = True

# ----- Record Schemas -----
class RecordCreateRequest(BaseModel):
    user_id: int
    record_data: str

class RecordUpdateRequest(BaseModel):
    user_id: Optional[int]
    record_data: Optional[str]


class RecordResponse(BaseModel):
    id: int
    user_id: int
    record_data: str

    class Config:
        orm_mode = True
