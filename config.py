from pydantic_settings import BaseSettings

class Config(BaseSettings):
    MYSQL_USER:str
    MYSQL_PASSWORD:str
    MYSQL_URL:str
    MYSQL_DB_NAME: str

    POSTGRES_USER: str
    POSTGRES_PASSWORD: str
    POSTGRES_URL:str
    POSTGRES_DB_NAME:str


    class Config:
        env_file = ".env"
        env_file_encoding = "utf-8"

config = Config()
