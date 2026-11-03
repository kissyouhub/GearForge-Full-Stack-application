
from pydantic import ConfigDict
from pydantic_settings import BaseSettings, SettingsConfigDict

class Settings(BaseSettings):
    model_config = SettingsConfigDict(env_file=".env", extra="ignore")
    database_url: str = ("postgresql+psycopg2://myuser:admin@gearforge-db:5432/gearforge_db_order")
    
settings = Settings()
    
    
class NotFoundError(Exception):
    pass
    