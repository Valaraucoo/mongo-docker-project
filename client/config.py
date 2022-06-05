from pydantic import BaseSettings


class AppConfig(BaseSettings):
    mongo_host: str = "db"
    mongo_port: int = 27017
    mongo_username: str = "root"
    mongo_password: str = "pass"


config = AppConfig()
