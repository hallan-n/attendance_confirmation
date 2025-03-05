import uuid
from sqlmodel import select
from model import GuestTable, GiftTable, GiftGuestTable
from infra.connection import Connection

def give_gift(guest: GuestTable, gift: GiftTable):
    with Connection() as conn:
        gift_guest = GiftGuestTable(guest_id=guest.id, gift_id=gift.id)
        conn.add(gift_guest)
        conn.commit()
        conn.refresh(gift_guest)
        return gift_guest


def revoke_give_gift(guest_id: GuestTable, gift_id):
    with Connection() as conn:
        statement = select(GiftGuestTable).where(
            GiftGuestTable.guest_id == uuid.UUID(guest_id),
            GiftGuestTable.gift_id == gift_id,
        )
        result = conn.exec(statement).first()

        if not result:
            return False

        conn.delete(result)
        conn.commit()
        return True
