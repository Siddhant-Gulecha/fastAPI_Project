from pydantic_settings import BaseSettings

class Config(BaseSettings):
    USER:str
    PASSWORD:str
    URL:str
    SYNC_POSTGRES_DB_NAME:str
    SYNC_MYSQL_DB_NAME:str
    ASYNC_POSTGRES_DB_NAME:str
    ASYNC_MYSQL_DB_NAME:str

    class Config:
        env_file = ".env"
        env_file_encoding = "utf-8"

config = Config()
