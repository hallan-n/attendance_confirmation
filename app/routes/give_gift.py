from fastapi import APIRouter, HTTPException
from infra.give_gift_persistence import (
    add_gift_guest,
    read_all_gift_guest,
    is_product_available,
    delete_give_gift,
)

route = APIRouter(prefix="/give_gift", tags=["Guest", "Admin"])


@route.get("/")
def get_all_give_gift():
    try:
        return read_all_gift_guest()
    except Exception as e:
        raise HTTPException(status_code=422, detail=f"Erro ao ler Gift Guest: {str(e)}")


@route.post("/")
def give_gift(guest_id: str, gift_id: int):
    try:
        is_available = is_product_available(gift_id)
        if not is_available:
            return add_gift_guest(guest_id, gift_id)
        else:
            raise HTTPException(
                status_code=422,
                detail="Este produto já foi por um convidado ou não está na lista.",
            )
    except Exception as e:
        raise HTTPException(status_code=422, detail=f"Erro ao dar um Gift: {str(e)}")


@route.delete("/")
def remove_gift_giver_by_gift_and_guest(guest_id: str, gift_id: int):
    try:
        return delete_give_gift(guest_id=guest_id, gift_id=gift_id)
    except Exception as e:
        raise HTTPException(
            status_code=422, detail=f"Erro ao deletar uma Gift: {str(e)}"
        )


@route.delete("/guest")
def remove_gift_giver_by_guest(guest_id: str):
    try:
        return delete_give_gift(guest_id=guest_id, gift_id=None)
    except Exception as e:
        raise HTTPException(
            status_code=422, detail=f"Erro ao deletar uma Gift: {str(e)}"
        )


@route.delete("/gift")
def remove_gift_giver_by_gift(gift_id: int):
    try:
        return delete_give_gift(gift_id=gift_id, guest_id=None)
    except Exception as e:
        raise HTTPException(
            status_code=422, detail=f"Erro ao deletar uma Gift: {str(e)}"
        )
