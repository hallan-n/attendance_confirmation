from sqlmodel import SQLModel, Field, Relationship
import uuid
from typing import List, Optional
from pydantic import EmailStr, BaseModel



class GuestTable(SQLModel, table=True):
    id: uuid.UUID = Field(default_factory=uuid.uuid4, primary_key=True)
    name: str = Field(..., min_length=3, max_length=100)
    email: Optional[EmailStr] = Field(default=None, max_length=255, unique=True)
    phone: str
    children: List["ChildrenTable"] = Relationship(back_populates="guest")


class ChildrenTable(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)  
    name: str = Field(..., min_length=3, max_length=100)
    guest_id: uuid.UUID = Field(foreign_key="guesttable.id")  
    guest: Optional[GuestTable] = Relationship(back_populates="children")


class ChildrenModel(BaseModel):
    id: int
    name: str


class GuestModel(BaseModel):
    id: str
    name: str
    email: Optional[EmailStr]
    phone: Optional[str]
    children: List[ChildrenModel] = []
