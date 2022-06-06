import random
import time
from logging import getLogger

from pymongo.collection import Collection

logger = getLogger(__name__)


def execute(alpha: Collection, beta: Collection) -> tuple[list, list]:
    logger.warning(f"[ex_one] Starting algorithm")

    max_n = 20
    res_t = []
    res_n = []

    for n in range(10, max_n, 50):
        logger.warning(f"[ex_one] n = {n} / {max_n} [{n/max_n*100:.2f}%]")

        l1 = [num for num in range(1, n + 1)]
        l2 = []
        start_time = time.time()

        while len(l2) < n:
            nr = random.randint(1, n)
            idx = 0
            for id in range(1, len(l2)):
                if l2[id - 1] == nr:
                    idx += 1

            if not l2:
                l2.append(nr)

        elapsed_time = time.time() - start_time

        logger.warning(f"[ex_one] Elapsed time = {elapsed_time}")

        res_n.append(n)
        res_t.append(elapsed_time)

    return res_t, res_n
