from sqlmodel import select
from infra.connection import Connection
from model import Login

def read_login(login: Login):
    with Connection() as conn:
        has_login = conn.exec(
            select(Login).where(
                Login.user == login.user, Login.password == login.password
            )
        ).first()
        return has_login


def read_login_by_id(login: Login):
    with Connection() as conn:
        guest = conn.get(Login, login.id)
        return guest


def create_login(login: Login):
    with Connection() as conn:
        conn.add(login)
        conn.commit()
        conn.refresh(login)
    return login
