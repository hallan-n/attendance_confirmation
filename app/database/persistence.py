import uuid
from sqlmodel import select
from database.connection import Connection
from database.model import Guest

def create_guest(guest: Guest):
    with Connection() as conn:
        guest.id = uuid.uuid4()
        conn.add(guest)
        conn.commit()
        conn.refresh(guest)
    return guest


def update_guest(guest: Guest):
    with Connection() as conn:
        has_guest = conn.get(Guest, uuid.UUID(guest.id))
        if has_guest:
            guest.id = uuid.UUID(guest.id)
            merged_guest = conn.merge(guest)
            conn.commit()
            conn.refresh(merged_guest)
            return merged_guest


def delete_guest(id: str):
    with Connection() as conn:
        guest = conn.get(Guest, uuid.UUID(id))
        if guest:
            conn.delete(guest)
            conn.commit()


def read_guest(id: str):
    with Connection() as conn:
        guest = conn.get(Guest, uuid.UUID(id))
        return guest


def read_all_guests():
    with Connection() as conn:
        guests = conn.exec(select(Guest)).all()
        return guests
