from dataclasses import dataclass
import os

@dataclass(frozen=True)
class Settings:
    database_url: str 
    
    
    
def get_settings () -> Settings:
    return Settings(
        database_url= os.getenv(
            "DATABASE_URL", 
            "postgresql+psycopg://postgres:admin@127.0.0.1:15432/postgres",
        ),
        
    )
    
    
