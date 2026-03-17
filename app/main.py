from fastapi import FastAPI
from routers import payments
from database import init_db, close_db
from contextlib import asynccontextmanager

@asynccontextmanager
async def lifespan(app: FastAPI):
    await init_db()
    yield
    await close_db()

app = FastAPI(lifespan=lifespan)

app.include_router(payments.router)

@app.get("/")
async def root():
    return {"message": "Payments API"}

@app.get("/health")
async def health():
    return {"status": "healthy"}