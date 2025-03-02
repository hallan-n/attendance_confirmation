from fastapi import APIRouter, HTTPException
from model import GuestTable
from persistence import (
    create_guest,
    read_guest,
    update_guest,
)


route = APIRouter()


@route.post("/", tags=["Guest", "Admin"])
def add_guest(guest: GuestTable):
    try:
        return create_guest(guest)
    except Exception as e:
        raise HTTPException(status_code=422, detail=f"Erro ao criar um Guest: {str(e)}")


@route.get("/{id}", tags=["Guest", "Admin"])
def get_guest(id: str):
    try:
        return read_guest(id)
    except Exception as e:
        raise HTTPException(status_code=422, detail=f"Erro ler um Guest: {str(e)}")


@route.put("/", tags=["Guest", "Admin"])
def att_guest(guest: GuestTable):
    try:
        return update_guest(guest)
    except Exception as e:
        raise HTTPException(
            status_code=422, detail=f"Erro ao atualizar um Guest: {str(e)}"
        )
