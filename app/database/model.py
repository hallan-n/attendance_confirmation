from sqlmodel import SQLModel, Field
import uuid
from typing import Optional
from pydantic import EmailStr


class Guest(SQLModel, table=True):
    id: uuid.UUID = Field(default_factory=uuid.uuid4, primary_key=True)
    name: str = Field(..., min_length=3, max_length=100)
    email: Optional[EmailStr] = Field(default=None, max_length=255, unique=True)
    phone: str
