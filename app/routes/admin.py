from fastapi import APIRouter, HTTPException
from model import GuestTable
from persistence import (
    create_guest,
    read_all_guests,
    delete_guest,
)

route = APIRouter()


@route.post("/", tags=["Admin"])
def add_guest(guest: GuestTable):
    try:
        return create_guest(guest)
    except Exception as e:
        raise HTTPException(status_code=422, detail=f"Erro ao criar um Guest: {str(e)}")


@route.delete("/admin", tags=["Admin"])
def revoke_guest(id: str):
    try:
        resp = delete_guest(id)
        return {"success": resp}
    except Exception as e:
        raise HTTPException(
            status_code=422, detail=f"Erro ao deletar uma Guest: {str(e)}"
        )


@route.get("/admin", tags=["Admin"])
def get_all_guests():
    try:
        return read_all_guests()
    except Exception as e:
        raise HTTPException(status_code=422, detail=f"Erro ler um Guest: {str(e)}")
