from sqlmodel import select, and_
from model import Gifter, Gift, GiftGiver
from infra.connection import Connection


def create_give_gift(gifter_giver: GiftGiver):
    with Connection() as conn:
        conn.add(gifter_giver)
        conn.commit()
        conn.refresh(gifter_giver)
        return gifter_giver


def gift_has_gifter(gift_id: int):
    with Connection() as conn:
        statement = select(GiftGiver).where(GiftGiver.gift_id == gift_id)
        result = conn.exec(statement).first()
        return bool(result)


def delete_give_gift(gift_id: int, gifter_id: int):
    with Connection() as conn:
        statement = select(GiftGiver).where(
            GiftGiver.gift_id == gift_id, GiftGiver.gifter_id == gifter_id
        )
        result = conn.exec(statement).first()

        if not result:
            return {"sucess": False}

        conn.delete(result)
        conn.commit()
        return {"sucess": True}
