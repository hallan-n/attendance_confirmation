from sqlmodel import SQLModel, Field, Relationship
import uuid
from typing import Optional, List
from pydantic import EmailStr


class GuestTable(SQLModel, table=True):
    id: uuid.UUID = Field(default_factory=uuid.uuid4, primary_key=True)
    name: str = Field(min_length=3, max_length=100)
    email: Optional[EmailStr] = Field(default=None, max_length=255, unique=True)
    phone: str = Field(min_length=3, max_length=100, default="")
    is_confirmed: bool = False
    description: str = Field(min_length=3, max_length=100, default="")

    gifts: List["GiftGuestTable"] = Relationship(back_populates="guest")


class GiftTable(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    thumb: str = Field(min_length=3, max_length=250)
    name: str = Field(min_length=3, max_length=100)
    description: str = Field(min_length=3, max_length=100)
    price: float

    givers: List["GiftGuestTable"] = Relationship(back_populates="gift")


class GiftGuestTable(SQLModel, table=True):
    guest_id: uuid.UUID = Field(foreign_key="guesttable.id", primary_key=True)
    gift_id: int = Field(foreign_key="gifttable.id", primary_key=True)

    guest: GuestTable = Relationship(back_populates="gifts")
    gift: GiftTable = Relationship(back_populates="givers")


class LoginTable(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    user: str
    password: str
