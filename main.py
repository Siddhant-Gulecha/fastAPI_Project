import asyncio
import time

from fastapi import FastAPI, Depends
from sqlalchemy.ext.asyncio.session import AsyncSession
from sqlalchemy.orm import Session
from database import SessionLocal, AsyncSessionLocal

app = FastAPI()

# Dependency for getting DB session
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.get("/check-sync-connection")
def read_root(db: Session = Depends(get_db)):
    return {"message": "Synchronous connection working!"}


# Dependency to get an async DB session
async def get_async_db():
    async with AsyncSessionLocal() as session:
        yield session

@app.get("/check-async-connection")
async def read_root(db: AsyncSession = Depends(get_async_db)):
    return {"message": "Async connection working!"}


@app.get("/simulate_load")
async def simulate_load(mode: str, db: str, requests: int):
    start = time.time()

    if mode == "async":
        tasks = [async_db_call(db) for _ in range(requests)]
        await asyncio.gather(*tasks)
    else:
        for _ in range(requests):
            sync_db_call(db)

    end = time.time()
    return {"total_time": end - start, "requests": requests}