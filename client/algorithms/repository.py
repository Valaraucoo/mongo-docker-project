import string
import random
from pydantic import BaseModel, Field

from pymongo.collection import Collection


def random_string_generator(size: int = 20, chars: str = string.ascii_uppercase + string.digits) -> str:
    return ''.join(random.choice(chars) for _ in range(size))


class MessageSchema(BaseModel):
    key: int
    value: str = Field(default_factory=random_string_generator)


def insert_one(coll: Collection, key: int) -> None:
    coll.insert_one(
        MessageSchema(key=key).dict()
    )


def clear_collection(coll: Collection) -> None:
    coll.delete_many({})


def fill_collection(coll: Collection, size: int = 100) -> Collection:
    clear_collection(coll)

    for key in range(1, size + 1):
        insert_one(coll, key)
    return coll


def find_message(coll: Collection, key: int) -> MessageSchema | None:
    if message := coll.find_one({"key": key}):
        return MessageSchema(**message)
    return None


def get_random_from_collection(coll: Collection) -> MessageSchema:
    messages = list(coll.find({}))
    return MessageSchema(**random.choice(messages))
