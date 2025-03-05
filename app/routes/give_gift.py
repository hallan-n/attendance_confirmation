from fastapi import APIRouter, HTTPException
from infra.give_gift_persistence import (
    add_gift_guest,
    is_product_available,
    delete_give_gift,
)

route = APIRouter(prefix="/give_gift", tags=["Guest","Admin"])


@route.post("/")
def give_gift(guest_id: str, gift_id: int):
    try:
        is_available = is_product_available(gift_id)
        if not is_available:
            raise HTTPException(
                status_code=422,
                detail="Este produto já foi por um convidado ou não está na lista.",
            )
        return add_gift_guest(guest_id, gift_id)
    except Exception as e:
        raise HTTPException(status_code=422, detail=f"Erro ao dar um Gift: {str(e)}")


@route.delete("/")
def remove_gift_giver(guest_id: str, gift_id: int):
    try:
        return delete_give_gift(guest_id, gift_id)
    except Exception as e:
        raise HTTPException(
            status_code=422, detail=f"Erro ao deletar uma Gift: {str(e)}"
        )
