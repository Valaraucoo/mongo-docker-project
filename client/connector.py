from pymongo import MongoClient

from config import config

tango_connection = MongoClient(
    host=config.tango_mongo_host,
    port=config.tango_mongo_port,
    username=config.mongo_username,
    password=config.mongo_password
)

sierra_connection = MongoClient(
    host=config.sierra_mongo_host,
    port=config.sierra_mongo_port,
    username=config.mongo_username,
    password=config.mongo_password
)
