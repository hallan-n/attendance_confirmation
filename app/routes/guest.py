from fastapi import APIRouter, HTTPException
from model import GuestTable
from infra.guest_persistence import (
    read_guest,
    update_guest,
)


route = APIRouter()


@route.get("/{id}", tags=["Guest"])
def get_guest(id: str):
    try:
        return read_guest(id)
    except Exception as e:
        raise HTTPException(status_code=422, detail=f"Erro ler um Guest: {str(e)}")


@route.put("/", tags=["Guest"])
def att_guest(guest: GuestTable):
    try:
        return update_guest(guest)
    except Exception as e:
        raise HTTPException(
            status_code=422, detail=f"Erro ao atualizar um Guest: {str(e)}"
        )
