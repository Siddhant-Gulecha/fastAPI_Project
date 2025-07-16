from sqlalchemy import create_engine
from sqlalchemy.ext.asyncio.engine import create_async_engine
from sqlalchemy.ext.asyncio.session import AsyncSession
from sqlalchemy.orm import sessionmaker, declarative_base
from config import config as Config


USER = Config.USER
PASSWORD = Config.PASSWORD
URL = Config.URL
SYNC_POSTGRES_DB_NAME = Config.SYNC_POSTGRES_DB_NAME
SYNC_MYSQL_DB_NAME = Config.SYNC_MYSQL_DB_NAME
ASYNC_POSTGRES_DB_NAME = Config.ASYNC_POSTGRES_DB_NAME
ASYNC_MYSQL_DB_NAME = Config.ASYNC_MYSQL_DB_NAME

# SYNChronus DB connection

SYNC_PG_DATABASE_URL = f"postgresql+psycopg2://%s:%s@%s/%s"%(USER, PASSWORD, URL, SYNC_POSTGRES_DB_NAME)
SYNC_MYSQL_DATABASE_URL = "mysql+pymysql://%s:%s@%s/%s"%(USER, PASSWORD, URL, SYNC_MYSQL_DB_NAME)

engine = create_engine(SYNC_PG_DATABASE_URL, echo=True)
SessionLocal = sessionmaker(bind=engine, autocommit=False, autoflush=False)
Base = declarative_base()


# ASYNChronus DB connection

ASYNC_PG_DATABASE_URL = f"postgresql+asyncpg://%s:%s@%s/%s"%(USER, PASSWORD, URL, ASYNC_POSTGRES_DB_NAME)
ASYNC_MYSQL_DATABASE_URL = "mysql+aiomysql://%s:%s@%s/%s"%(USER, PASSWORD, URL, ASYNC_MYSQL_DB_NAME)

async_engine = create_async_engine(ASYNC_PG_DATABASE_URL, echo=True)
AsyncSessionLocal = sessionmaker(bind=async_engine, class_=AsyncSession, expire_on_commit=False)

