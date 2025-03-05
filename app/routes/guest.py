from fastapi import APIRouter, Depends, HTTPException
from security import decode_token
from model import GuestTable
from infra.guest_persistence import (
    create_guest,
    read_all_guests,
    delete_guest,
    read_guest,
    update_guest,
)


route = APIRouter(prefix="/guest")


@route.get("/{id}", tags=["Admin","Guest"])
def get_guest(id: str):
    try:
        return read_guest(id)
    except Exception as e:
        raise HTTPException(status_code=422, detail=f"Erro ler um Guest: {str(e)}")


@route.put("/", tags=["Admin","Guest"])
def att_guest(guest: GuestTable):
    try:
        return update_guest(guest)
    except Exception as e:
        raise HTTPException(
            status_code=422, detail=f"Erro ao atualizar um Guest: {str(e)}"
        )

@route.post("/", tags=["Admin"])
def add_guest(guest: GuestTable, token: dict = Depends(decode_token)):
    try:
        return create_guest(guest)
    except Exception as e:
        raise HTTPException(status_code=422, detail=f"Erro ao criar um Guest: {str(e)}")


@route.delete("/", tags=["Admin"])
def revoke_guest(id: str, token: dict = Depends(decode_token)):
    try:
        resp = delete_guest(id)
        return {"success": resp}
    except Exception as e:
        raise HTTPException(
            status_code=422, detail=f"Erro ao deletar uma Guest: {str(e)}"
        )


@route.get("/", tags=["Admin"])
def get_all_guests(token: dict = Depends(decode_token)):
    try:
        return read_all_guests()
    except Exception as e:
        raise HTTPException(status_code=422, detail=f"Erro ler um Guest: {str(e)}")
