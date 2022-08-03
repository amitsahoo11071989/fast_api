from pydantic import BaseSettings

class Settings(BaseSettings):
    database_host: str
    database_port: str
    database_username: str
    database_password: str
    database_name: str
    token_secret_key: str
    token_algorithm: str
    token_access_expire_minutes: int

    class Config:
        env_file = ".env"



setting = Settings()