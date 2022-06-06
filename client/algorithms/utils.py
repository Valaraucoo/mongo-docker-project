import string
import random
from logging import getLogger

from pymongo.collection import Collection

logger = getLogger(__name__)


def random_string_generator(size: int = 20, chars: str = string.ascii_uppercase + string.digits) -> str:
    return ''.join(random.choice(chars) for _ in range(size))


def fill_collection(coll: Collection, size: int = 100) -> None:
    logger.warning("[fill_collection] Removing collection content")
    # coll.remove()

    logger.warning("[fill_collection] Started filling collection")

    for key in range(size):
        coll.insert_one({
            "key": key,
            "value": random_string_generator()
        })
