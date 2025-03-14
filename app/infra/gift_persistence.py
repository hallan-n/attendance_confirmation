from sqlmodel import select
from model import GiftTable
from infra.connection import Connection


def create_gift(gift: GiftTable):
    with Connection() as conn:
        del gift.id
        conn.add(gift)
        conn.commit()
        conn.refresh(gift)
    return gift


def read_gift(id: int):
    with Connection() as conn:
        gift = conn.get(GiftTable, id)
        return gift


def read_all_gifts():
    with Connection() as conn:
        gifts = conn.exec(select(GiftTable)).all()
        return gifts


def update_gift(gift: GiftTable):
    with Connection() as conn:
        has_gift = conn.get(GiftTable, gift.id)
        if has_gift:
            merged_gift = conn.merge(gift)
            conn.commit()
            conn.refresh(merged_gift)
            return merged_gift


def delete_gift(id: int):
    with Connection() as conn:
        user = conn.get(GiftTable, id)
        if user:
            conn.delete(user)
            conn.commit()
            return True
        return False
