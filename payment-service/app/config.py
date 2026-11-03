
from pydantic import ConfigDict
from pydantic_settings import BaseSettings, SettingsConfigDict

class Settings(BaseSettings):
    model_config = SettingsConfigDict(env_file=".env", extra="ignore")
    database_url: str = ("postgresql+psycopg2://payments:payments@localhost:5435/payments")
    
settings = Settings()
    
    
class NotFoundError(Exception):
    pass
    