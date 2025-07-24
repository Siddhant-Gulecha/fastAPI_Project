from fastapi import FastAPI, Depends
from sqlalchemy.ext.asyncio.session import AsyncSession
from sqlalchemy.orm import Session
from database import get_sync_mysql_db, get_sync_postgres_db, get_async_mysql_db, get_async_postgres_db
from controller import sync_pg_controller, async_pg_controller

app = FastAPI()

app.include_router(async_pg_controller.router)
app.include_router(sync_pg_controller.router)


@app.get("/check-sync-mysql-connection")
def check_sync_mysql_connection(db: Session = Depends(get_sync_mysql_db)):
    return {"message": "connection working!"}


@app.get("/check-sync-postgres-connection")
def check_sync_postgres_connection(db: Session = Depends(get_sync_postgres_db)):
    return {"message": "connection working!"}


@app.get("/check-async-mysql-connection")
async def check_async_mysql_connection(db: AsyncSession = Depends(get_async_mysql_db)):
    return {"message": "connection working!"}


@app.get("/check-async-postgres-connection")
async def check_async_postgres_connection(db: AsyncSession = Depends(get_async_postgres_db)):
    return {"message": "connection working!"}


