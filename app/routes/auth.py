from security import create_access_token, decode_token
from fastapi import APIRouter, Depends, HTTPException
from model import LoginTable
from infra.auth_persistence import read_login, create_login

route = APIRouter()


@route.post("/admin/login", tags=["Auth"])
def sign_in(login: LoginTable):
    login = read_login(login)
    if not bool(login):
        raise HTTPException(404, "Login não encontrado!")

    data = {"sub": login.user, "id": login.id}
    access_token = create_access_token(data=data)
    return {"access_token": access_token, "token_type": "bearer"}


@route.post("/admin/create", tags=["Auth"])
def add_login(login: LoginTable, token: dict = Depends(decode_token)):
    try:
        login.id = None
        return create_login(login)
    except Exception as e:
        raise HTTPException(status_code=422, detail=f"Erro ao criar um Login: {str(e)}")
