from dataclasses import dataclass
import os

@dataclass(frozen=True)
class Settings:
    database_url: str 
    cors_origins: list[str]
    
    
def get_settings () -> Settings:
    return Settings(
        database_url= os.getenv(
            "DATABASE_URL", 
            "postgresql+psycopg2://myuser:admin@gearforge-db:5432/gearforge_db",
        ),
        cors_origins=["*"],
        
    )
    
    
