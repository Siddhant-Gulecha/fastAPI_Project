from fastapi import FastAPI, Depends
from sqlalchemy.ext.asyncio.session import AsyncSession
from sqlalchemy.orm import Session
from database import get_sync_mysql_db, get_sync_postgres_db, get_async_mysql_db, get_async_postgres_db, Base, \
    sync_pg_engine, sync_mysql_engine
from routers import sync_crud, async_crud

app = FastAPI()

app.include_router(sync_crud.router)
app.include_router(async_crud.router)


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


