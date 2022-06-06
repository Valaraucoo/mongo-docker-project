from pydantic import BaseSettings


class AppConfig(BaseSettings):
    tango_mongo_host: str = "tango"
    tango_mongo_port: int = 27017

    sierra_mongo_host: str = "sierra"
    sierra_mongo_port: int = 27017

    mongo_username: str = "root"
    mongo_password: str = "pass"

    db_name: str = "database"


config = AppConfig()
