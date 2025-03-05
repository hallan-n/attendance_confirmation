from sqlmodel import select
from infra.connection import Connection
from model import LoginTable


def read_login(login: LoginTable):
    with Connection() as conn:
        has_login = conn.exec(
            select(LoginTable).where(
                LoginTable.user == login.user, LoginTable.password == login.password
            )
        ).first()
        return has_login


def read_login_by_id(login: LoginTable):
    with Connection() as conn:
        guest = conn.get(LoginTable, login.id)
        return guest


def create_login(login: LoginTable):
    with Connection() as conn:
        conn.add(login)
        conn.commit()
        conn.refresh(login)
    return login
