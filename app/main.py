from dotenv import load_dotenv
from os import getenv
from fastapi import FastAPI, HTTPException
import uvicorn
from fastapi.middleware.cors import CORSMiddleware
from model import LoginTable
from routes.guest import route as guest
from routes.auth import route as auth
from routes.gift import route as gift
# from routes.gifter import route as gifter

from infra.auth_persistence import create_login, read_login_by_id
import logging

load_dotenv()

setup_done = False


def setup():
    global setup_done
    if not setup_done:
        try:
            user = getenv("FIRST_SUPERUSER")
            password = getenv("FIRST_SUPERUSER_PASSWORD")

            if not user or not password:
                raise ValueError("Credenciais de SuperADM não encontrado .env.")

            has_login = read_login_by_id(LoginTable(id=1, user=user, password=password))
            if has_login:
                print("SuperADM já existe!")
            else:
                create_login(LoginTable(user=user, password=password))
                print("SuperADM criado com sucesso!")
            setup_done = True
        except Exception as e:
            print(f"Erro ao criar SuperADM: {str(e)}")
            setup_done = False
            logging.error(f"Erro ao criar SuperADM: {str(e)}")
            raise HTTPException(
                status_code=422, detail=f"Erro ao criar um Super User: {str(e)}"
            )

setup()

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

app.include_router(guest)
app.include_router(auth)
app.include_router(gift)
# app.include_router(gifter)


if __name__ == "__main__":
    uvicorn.run(
        "main:app",
        host="localhost",
        port=8000,
        reload=True,
    )
