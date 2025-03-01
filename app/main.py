from fastapi import FastAPI, HTTPException
import uvicorn
from model import GuestTable
from persistence import create_guest, read_guest, read_all_guests, update_guest, delete_guest
from fastapi.middleware.cors import CORSMiddleware


app = FastAPI(title="API de Confirmação de Presença")
origins = [
    "http://localhost",
    "http://localhost:5173",
]
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.post('/', tags=['Guest', 'Admin'])
def add_guest(guest: GuestTable):
    try:
        return create_guest(guest)
    except Exception as e:
        raise HTTPException(status_code=422, detail=f"Erro ao criar um Guest: {str(e)}")

@app.get('/{id}', tags=['Guest', 'Admin'])
def get_guest(id: str):
    try:
        return read_guest(id)
    except Exception as e:
        raise HTTPException(status_code=422, detail=f"Erro ler um Guest: {str(e)}")


@app.put('/', tags=['Guest', 'Admin'])
def att_guest(guest: GuestTable):
    try:
        return update_guest(guest)
    except Exception as e:
        raise HTTPException(status_code=422, detail=f"Erro ao atualizar um Guest: {str(e)}")

@app.delete('/', tags=['Admin'])
def revoke_guest(id: str):
    try:
        resp = delete_guest(id)
        return {'success': resp}
    except Exception as e:
        raise HTTPException(status_code=422, detail=f"Erro ao deletar uma Guest: {str(e)}")


@app.get('/', tags=['Admin'])
def get_all_guests():
    try:
        return read_all_guests()
    except Exception as e:
        raise HTTPException(status_code=422, detail=f"Erro ler um Guest: {str(e)}")


if __name__ == "__main__":
    uvicorn.run(
        "main:app",
        host="localhost",
        port=8000,
        reload=True,
    )
