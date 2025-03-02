from security import create_access_token
from fastapi import APIRouter, HTTPException
from model import Login
from persistence import read_login

route = APIRouter()



@route.post("/admin/login", tags=["Admin"])
def sign_in(login: Login):
    login = read_login(login)
    if not bool(login):
        raise HTTPException(404, "Login não encontrado!")

    data = {"sub": login.user, "id": login.id}
    access_token = create_access_token(data=data)
    return {"access_token": access_token, "token_type": "bearer"}
