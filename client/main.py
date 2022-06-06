from logging import getLogger

from pymongo.collection import Collection
from pymongo.database import Database

from algorithms import executor
from config import config
from connector import tango_connection, sierra_connection

logger = getLogger(__name__)


if __name__ == "__main__":
    tango: Database = tango_connection[config.db_name]
    sierra: Database = sierra_connection[config.db_name]

    alpha: Collection = tango.alpha
    beta: Collection = tango.beta
    gamma: Collection = sierra.gamma

    one_instance_times = executor.execute(alpha, beta, num_iteration=400, step=20)
    two_instances_times = executor.execute(alpha, gamma, num_iteration=400, step=20)

    logger.warning(f"1. One instance times = {one_instance_times}")
    logger.warning(f"2. Two instances times = {two_instances_times}")
