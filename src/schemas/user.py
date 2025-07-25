from datetime import datetime
from uuid import UUID

from pydantic import BaseModel, EmailStr, Field


class UserCreateSchema(BaseModel):
    name: str = Field(..., example="Fernando")
    surname: str = Field(..., example="Pacheco")
    email: EmailStr = Field(..., example="fernando@example.com")
    password: str = Field(..., min_length=6, example="123456")

    class Config:
        from_attributes = True


class UserResponseSchema(BaseModel):
    id: UUID
    name: str
    surname: str
    email: EmailStr
    created_at: datetime
    updated_at: datetime

    class Config:
        from_attributes = True
