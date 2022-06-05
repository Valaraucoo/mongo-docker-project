from pymongo import MongoClient

from config import config

connection = MongoClient(
    host=config.mongo_host,
    port=config.mongo_port,
    username=config.mongo_username,
    password=config.mongo_password
)
