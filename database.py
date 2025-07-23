import asyncio

from sqlalchemy import create_engine
from sqlalchemy.ext.asyncio.engine import create_async_engine
from sqlalchemy.ext.asyncio.session import AsyncSession
from sqlalchemy.orm import sessionmaker, declarative_base
from config import config as Config


MYSQL_USER = Config.MYSQL_USER
MYSQL_PASSWORD = Config.MYSQL_PASSWORD
MYSQL_URL = Config.MYSQL_URL
MYSQL_DB_NAME = Config.MYSQL_DB_NAME

POSTGRES_USER = Config.POSTGRES_USER
POSTGRES_PASSWORD = Config.POSTGRES_PASSWORD
POSTGRES_URL = Config.POSTGRES_URL
POSTGRES_DB_NAME = Config.POSTGRES_DB_NAME


# SYNChronus DB connection

SYNC_PG_DATABASE_URL = f"postgresql+psycopg2://%s:%s@%s/%s"%(POSTGRES_USER, POSTGRES_PASSWORD, POSTGRES_URL, POSTGRES_DB_NAME)
SYNC_MYSQL_DATABASE_URL = "mysql+pymysql://%s:%s@%s/%s"%(MYSQL_USER, MYSQL_PASSWORD, MYSQL_URL, MYSQL_DB_NAME)


sync_pg_engine = create_engine(SYNC_PG_DATABASE_URL, echo=True)
SessionLocalPostgres = sessionmaker(bind=sync_pg_engine, autocommit=False, autoflush=False)

sync_mysql_engine = create_engine(SYNC_MYSQL_DATABASE_URL, echo=True)
SessionLocalMySQL = sessionmaker(bind=sync_mysql_engine, autocommit=False, autoflush=False)

Base = declarative_base()


# ASYNChronus DB connection

ASYNC_PG_DATABASE_URL = f"postgresql+asyncpg://%s:%s@%s/%s"%(POSTGRES_USER, POSTGRES_PASSWORD, POSTGRES_URL, POSTGRES_DB_NAME)
ASYNC_MYSQL_DATABASE_URL = "mysql+aiomysql://%s:%s@%s/%s"%(MYSQL_USER, MYSQL_PASSWORD, MYSQL_URL, MYSQL_DB_NAME)


async_pg_engine = create_async_engine(ASYNC_PG_DATABASE_URL, echo=True)
AsyncSessionLocalPostgres = sessionmaker(bind=async_pg_engine, class_=AsyncSession, expire_on_commit=False)


async_mysql_engine = create_async_engine(ASYNC_MYSQL_DATABASE_URL, echo=True)
AsyncSessionLocalMySQL = sessionmaker(bind=async_mysql_engine, class_=AsyncSession, expire_on_commit=False)


# Dependency for getting sync DB session
def get_sync_mysql_db():
    db = SessionLocalMySQL()
    try:
        yield db
    finally:
        db.close()

def get_sync_postgres_db():
    db = SessionLocalPostgres()
    try:
        yield db
    finally:
        db.close()


# Dependency to get an async DB session
async def get_async_mysql_db():
    async with AsyncSessionLocalMySQL() as session:
        yield session


async def get_async_postgres_db():
    async with AsyncSessionLocalPostgres() as session:
        yield session


