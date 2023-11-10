import os

from dotenv import load_dotenv
from pydantic import BaseConfig


class GlobalConfig(BaseConfig):

    title: str = "Title"
    version: str = "1.0.0"
    description: str = "Description here"
    docs_url: str = "/docs"
    redoc_url: str = "/redoc"
    openapi_url: str = "/openapi.json"
    api_prefix: str = "/api"
    debug: bool = True
    
    postgres_user: str = 'postgres'
    postgres_password: str = 'postgres_password'
    postgres_server: str = 'db_postgres'
    postgres_port: int = 5432
    postgres_db_name: str = 'testando'
    db_echo_log: bool = True

    '''@property
    def sync_database_url(self) -> str:
        return f"postgresql://{self.postgres_user}:{self.postgres_password}@{self.postgres_server}:{self.postgres_port}/{self.postgres_db_name}"'''
    
    @property
    def sync_database_url(self) -> str:
        return f"sqlite:///meu_banco.db"
    
    '''@property
    def async_database_url(self) -> str:
        return f"postgresql+asyncpg://{self.postgres_user}:{self.postgres_password}@{self.postgres_server}:{self.postgres_port}/{self.postgres_db_name}"'''
    
    @property
    def async_database_url(self) -> str:
        return f"sqlite+aiosqlite:///meu_banco.db"
