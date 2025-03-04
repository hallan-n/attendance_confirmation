from sqlmodel import SQLModel, Field, Relationship
import uuid
from typing import Optional, List
from pydantic import EmailStr, field_validator
import re


class GuestTable(SQLModel, table=True):
    id: uuid.UUID = Field(default_factory=uuid.uuid4, primary_key=True)
    name: str = Field(..., min_length=3, max_length=100)
    email: Optional[EmailStr] = Field(default=None, max_length=255, unique=True)
    phone: str = Field(min_length=3, max_length=100, default="")
    is_confirmed: bool = False
    description: str = Field(min_length=3, max_length=100, default="")
    child_1: str = Field(min_length=3, max_length=100, default="")
    child_2: str = Field(min_length=3, max_length=100, default="")
    child_3: str = Field(min_length=3, max_length=100, default="")
    child_4: str = Field(min_length=3, max_length=100, default="")
    child_5: str = Field(min_length=3, max_length=100, default="")
    child_6: str = Field(min_length=3, max_length=100, default="")
    child_7: str = Field(min_length=3, max_length=100, default="")
    child_8: str = Field(min_length=3, max_length=100, default="")
    child_9: str = Field(min_length=3, max_length=100, default="")
    child_10: str = Field(min_length=3, max_length=100, default="")


class Login(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    user: str
    password: str


class GiftGiver(SQLModel, table=True):
    gifter_id: int = Field(foreign_key="gifter.id", primary_key=True)
    gift_id: int = Field(foreign_key="gift.id", primary_key=True)


class Gifter(SQLModel, table=True):
    id: Optional[int] = Field(primary_key=True)
    name: str = Field(..., min_length=3, max_length=100)
    email: EmailStr = Field(..., min_length=3, max_length=255, unique=True)
    phone: str
    password: str = Field(..., min_length=3, max_length=100)
    gifts: List["Gift"] = Relationship(back_populates="gifters", link_model=GiftGiver)

    @field_validator("phone", mode="before")
    def validate_phone(cls, value):
        pattern = r"(\()?\d{0,2}(\))?\s{0,}\d{0,1}\s{0,}\d{4}(-)?\d{4}$"
        if not re.match(pattern, value):
            raise ValueError("Telefone no formato incorreto.")
        return value


class Gift(SQLModel, table=True):
    id: Optional[int] = Field(primary_key=True)
    name: str = Field(..., min_length=3, max_length=100)
    description: str = Field(..., min_length=3, max_length=100)
    price: float
    gifters: List[Gifter] = Relationship(back_populates="gifts", link_model=GiftGiver)


class Admin(SQLModel, table=True):
    id: Optional[int] = Field(primary_key=True)
    email: EmailStr
    password: str = Field(..., min_length=3, max_length=100)
