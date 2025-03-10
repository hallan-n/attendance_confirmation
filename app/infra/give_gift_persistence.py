import uuid
from sqlmodel import select
from model import GiftGuestTable
from infra.connection import Connection


def read_all_gift_guest():
    with Connection() as conn:
        gifts_guests = conn.exec(select(GiftGuestTable)).all()
        return gifts_guests


def add_gift_guest(guest_id: int, gift_id: int):
    with Connection() as conn:
        gift_guest = GiftGuestTable(guest_id=uuid.UUID(guest_id), gift_id=gift_id)
        conn.add(gift_guest)
        conn.commit()
        conn.refresh(gift_guest)
        return gift_guest


def delete_give_gift(guest_id = None, gift_id = None):
    with Connection() as conn:
        if guest_id and gift_id:
            statement = select(GiftGuestTable).where(
                GiftGuestTable.guest_id == uuid.UUID(guest_id),
                GiftGuestTable.gift_id == gift_id,
            )
        elif guest_id:
            statement = select(GiftGuestTable).where(
                GiftGuestTable.guest_id == uuid.UUID(guest_id),
            )
        elif gift_id:
            statement = select(GiftGuestTable).where(
                GiftGuestTable.gift_id == gift_id,
            )
        result = conn.exec(statement).first()

        if not result:
            return False

        conn.delete(result)
        conn.commit()
        return True


def is_product_available(gift_id: int):
    with Connection() as conn:
        statement = select(GiftGuestTable).where(
            GiftGuestTable.gift_id == gift_id,
        )
        result = conn.exec(statement).first()
        return bool(result)
