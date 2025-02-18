from fastapi import FastAPI, HTTPException
import uvicorn
from database.model import Guest
from database.persistence import create_guest, read_all_guests, read_guest, update_guest
import uuid

app = FastAPI(title="API de Confirmação de Presença")

@app.post('/')
def add_guest(guest: Guest):
    try:
        create_guest(guest)
        return guest
    except:
        raise HTTPException(status_code=422, detail='Erro ao criar um Guest.')
    
@app.put('/')
def att_guest(guest: Guest):
    return update_guest(guest)
    # try:
    # except:
    #     raise HTTPException(status_code=422, detail='Erro ao atualizar um Guest.')


@app.get('/{id}')
def get_guest(id: str):
    try:
        return read_guest(id)
    except:
        raise HTTPException(status_code=404, detail='Erro ao pegar um Guest.')

@app.get('/')
def get_all_guests():
    try:
        return read_all_guests()
    except:
        raise HTTPException(status_code=404, detail='Erro ao pegar um Guest.')


if __name__ == "__main__":
    uvicorn.run(
        "main:app",
        host="localhost",
        port=8000,
        reload=True,
    )
