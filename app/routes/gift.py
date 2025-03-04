from fastapi import APIRouter, Depends, HTTPException
from security import decode_token
from model import Gift
from infra.gift_persistence import create_gift, read_gift, update_gift, delete_gift, read_gifts

route = APIRouter(prefix="/gift", tags=["Admin"])


def _is_admin(token: dict):
    return True if token["role"] == "admin" else False


@route.post("/")
def add_gift(gift: Gift, token: dict = Depends(decode_token)):
    if  gift.id >= 0:
        del gift.id
    if _is_admin(token):
        return create_gift(gift)
    raise HTTPException(status_code=401, detail="Login não encontrado!")


@route.get("/all", tags=["Presenteador"])
def get_gifts(offset: int = 0, limit: int = 10, token: dict = Depends(decode_token)):
    try:
        return read_gifts(offset, limit)
    except:
        raise HTTPException(status_code=401, detail="Login não encontrado!")


@route.get("/", tags=["Presenteador"])
def get_gift(id: int, token: dict = Depends(decode_token)):
    try:
        return read_gift(id)
    except:
        raise HTTPException(status_code=401, detail="Login não encontrado!")

@route.put("/")
def edit_gift(gift: Gift, token: dict = Depends(decode_token)):
    if _is_admin(token):
        return update_gift(gift)
    raise HTTPException(status_code=401, detail="Login não encontrado!")


@route.delete("/")
def remove_gift(id: int, token: dict = Depends(decode_token)):
    if _is_admin(token):
        return delete_gift(id)
    raise HTTPException(status_code=401, detail="Login não encontrado!")
