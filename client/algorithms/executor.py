import time
from logging import getLogger

from pymongo.collection import Collection

from . import repository
from .repository import MessageSchema
from ..config import config

logger = getLogger(__name__)


def execute(alpha: Collection, beta: Collection, max_n: int = config.max_n, step: int = config.step) -> list[float]:
    logger.warning(f"Started executing algorithm; max_n={max_n}; step={step};")
    times = []

    for n in range(0, max_n, step):
        logger.warning(f"Executing algorithm; iteration: {n} [{n/max_n*100:.2f}%]")
        repository.fill_collection(alpha, size=n)
        repository.clear_collection(beta)

        start_time = time.time()

        count = 0
        while count < n - 1:
            message: MessageSchema = repository.get_random_from_collection(alpha)
            for k in range(1, message.key):
                if not repository.find_message(beta, key=k):
                    repository.insert_one(beta, key=k)
                    count += 1

        elapsed_time = time.time() - start_time
        times.append(elapsed_time)

    return times
