import uuid
from sqlmodel import select
from connection import Connection
from model import GuestTable, Login


def create_guest(guest: GuestTable):
    with Connection() as conn:
        guest.id = uuid.uuid4()
        conn.add(guest)
        conn.commit()
        conn.refresh(guest)
    return guest


def update_guest(guest: GuestTable):
    with Connection() as conn:
        has_guest = conn.get(GuestTable, uuid.UUID(guest.id))
        if has_guest:
            guest.id = uuid.UUID(guest.id)
            merged_guest = conn.merge(guest)
            conn.commit()
            conn.refresh(merged_guest)
            return merged_guest


def delete_guest(id: str):
    with Connection() as conn:
        guest = conn.get(GuestTable, uuid.UUID(id))
        if guest:
            conn.delete(guest)
            conn.commit()
            return True 
        return False

def read_guest(id: str):
    with Connection() as conn:
        guest = conn.get(GuestTable, uuid.UUID(id))
        return guest


def read_all_guests():
    with Connection() as conn:
        guests = conn.exec(select(GuestTable)).all()
        return guests


def read_login(login: Login):
    with Connection() as conn:
        guest = conn.get(GuestTable, login.id)
        return guest
