from dotenv import load_dotenv
from fastapi import FastAPI
import uvicorn
from fastapi.middleware.cors import CORSMiddleware
from routes.guest import route as guest
from routes.auth import route as auth
from routes.gift import route as gift
from routes.give_gift import route as gifter

load_dotenv(override=True)

setup_done = False

app = FastAPI(title="API de Confirmação de Presença")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(guest)
app.include_router(auth)
app.include_router(gift)
app.include_router(gifter)

if __name__ == "__main__":
    uvicorn.run(
        "main:app",
        host="0.0.0.0",
        port=8000,
        reload=True,
    )
