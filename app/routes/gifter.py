from fastapi import APIRouter, Depends
from fastapi.exceptions import HTTPException
from infra.give_gift_persistence import delete_give_gift, gift_has_gifter, create_give_gift
from model import Gifter, GiftGiver
from security import decode_token, hashed
from infra.gift_persistence import read_gift
from infra.gifter_persistence import create_gifter, read_gifter


route = APIRouter(prefix="/gifter", tags=["Presenteador"])


@route.post("/register")
def register_gifter(gifter: Gifter):
    if gifter.id >= 0:
        del gifter.id
    gifter.password = hashed(gifter.password)
    return create_gifter(gifter)

@route.get("/")
def get_gifter(token: dict = Depends(decode_token)):
    return read_gifter(token["id"])


@route.post("/")
def give_gift(gift_id: int, token: dict = Depends(decode_token)):
    has_gift = read_gift(gift_id)
    has_gifter = gift_has_gifter(gift_id)
    if not has_gift or has_gifter:
        raise HTTPException(status_code=401, detail='Presente não encontrado ou já possui presenteador.')
    return create_give_gift(GiftGiver(gift_id=gift_id, gifter_id=token['id']))

@route.delete("/")
def revoke_gift(gift_id: int, token: dict = Depends(decode_token)):
    return delete_give_gift(gift_id, token['id'])
