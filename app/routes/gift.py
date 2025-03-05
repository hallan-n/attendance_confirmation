from fastapi import APIRouter, Depends, HTTPException
from security import decode_token
from model import GiftTable
from infra.gift_persistence import create_gift, read_gift, update_gift, delete_gift, read_all_gifts

route = APIRouter(prefix="/gift", tags=["Admin"])


@route.post("/")
def add_gift(gift: GiftTable, token: dict = Depends(decode_token)):
    try:
        return create_gift(gift)
    except Exception as e:
        raise HTTPException(status_code=422, detail=f"Erro ao criar um Gift: {str(e)}")


@route.get("/")
def get_all_gifts():
    try:
        return read_all_gifts()
    except Exception as e:
        raise HTTPException(status_code=422, detail=f"Erro ler um Gifts: {str(e)}")


@route.get("/{id}")
def get_gift(id: int):
    try:
        return read_gift(id)
    except Exception as e:
        raise HTTPException(status_code=422, detail=f"Erro ler um Gift: {str(e)}")


@route.put("/")
def att_gift(gift: GiftTable, token: dict = Depends(decode_token)):
    try:
        return update_gift(gift)
    except Exception as e:
        raise HTTPException(
            status_code=422, detail=f"Erro ao atualizar um Gift: {str(e)}"
        )

@route.delete("/")
def remove_gift(id: int, token: dict = Depends(decode_token)):
    try:
        resp = delete_gift(id)
        return {"success": resp}
    except Exception as e:
        raise HTTPException(
            status_code=422, detail=f"Erro ao deletar uma Gift: {str(e)}"
        )
