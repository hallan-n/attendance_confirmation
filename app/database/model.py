from sqlmodel import SQLModel, Field
import uuid
from typing import Optional
from pydantic import EmailStr


class GuestTable(SQLModel, table=True):
    id: uuid.UUID = Field(default_factory=uuid.uuid4, primary_key=True)
    name: str = Field(..., min_length=3, max_length=100)
    email: Optional[EmailStr] = Field(default=None, max_length=255, unique=True)
    phone: str = Field(min_length=3, max_length=100, default='')
    is_confirmed: bool = False
    description: str = Field(min_length=3, max_length=100, default="")
    child_1: str = Field(min_length=3, max_length=100, default='')
    child_2: str = Field(min_length=3, max_length=100, default='')
    child_3: str = Field(min_length=3, max_length=100, default='')
    child_4: str = Field(min_length=3, max_length=100, default='')
    child_5: str = Field(min_length=3, max_length=100, default='')
    child_6: str = Field(min_length=3, max_length=100, default='')
    child_7: str = Field(min_length=3, max_length=100, default='')
    child_8: str = Field(min_length=3, max_length=100, default='')
    child_9: str = Field(min_length=3, max_length=100, default='')
    child_10: str = Field(min_length=3, max_length=100, default='')
