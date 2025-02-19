import uuid
from sqlmodel import select
from database.connection import Connection
from database.model import GuestTable, ChildrenTable


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


def read_guest(id: str):
    with Connection() as conn:
        guest = conn.get(GuestTable, uuid.UUID(id))
        return guest


def read_all_guests():
    with Connection() as conn:
        guests = conn.exec(select(GuestTable)).all()
        return guests


def create_children(children: ChildrenTable):
    with Connection() as conn:
        conn.add(children)
        conn.commit()
        conn.refresh(children)
    return children


def update_children(children: ChildrenTable):
    with Connection() as conn:
        has_children = conn.get(ChildrenTable, children.id)
        if has_children:
            merged_children = conn.merge(children)
            conn.commit()
            conn.refresh(merged_children)
            return merged_children


def delete_children(id: int):
    with Connection() as conn:
        children = conn.get(ChildrenTable, id)
        if children:
            conn.delete(children)
            conn.commit()


def read_children(id: int):
    with Connection() as conn:
        children = conn.get(ChildrenTable, id)
        return children


def read_all_children():
    with Connection() as conn:
        children = conn.exec(select(ChildrenTable)).all()
        return children
