from dotenv import load_dotenv
from os import getenv
from fastapi import FastAPI, HTTPException
import uvicorn
from fastapi.middleware.cors import CORSMiddleware
from model import Login
from routes.admin import route as admin
from routes.guest import route as guest
from routes.auth import route as auth
from persistence import create_login

load_dotenv()
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

app.include_router(admin)
app.include_router(guest)
app.include_router(auth)

try:
    user = getenv("FIRST_SUPERUSER")
    password = getenv("FIRST_SUPERUSER_PASSWORD")
    create_login(Login(user=user, password=password))
except Exception as e:
    raise HTTPException(
        status_code=422, detail=f"Erro ao criar um Super User: {str(e)}"
    )


if __name__ == "__main__":
    uvicorn.run(
        "main:app",
        host="localhost",
        port=8000,
        reload=True,
    )
