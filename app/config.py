# from pydantic import BaseSettings
from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    db_driver:str
    db_server:str
    db_port:str
    db_name:str
    db_encrypt:str
    db_trust_cert:str
    db_mars:str
    db_app_name:str
    db_user:str|None=None
    db_password:str|None=None
    db_auth:str

    class Config:
        env_file=".env.windows"
        env_file_encoding="utf-8"
        extra="allow"

appSettings = Settings()
