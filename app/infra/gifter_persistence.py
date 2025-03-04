from sqlmodel import select
from model import Gifter
from infra.connection import Connection


def create_gifter(gifter: Gifter):
    with Connection() as conn:
        conn.add(gifter)
        conn.commit()
        conn.refresh(gifter)
    return {"sucess": True}


def read_gifter(id: int):
    with Connection() as conn:
        gifter = conn.get(Gifter, id)
        return gifter


def read_gifter_by_email(email: str):
    with Connection() as conn:
        statement = select(Gifter).where(Gifter.email == email)
        gifter = conn.exec(statement).first()
        return gifter
