from logging import getLogger

from pymongo.database import Database

from algorithms import executor
from config import config
from connector import tango_connection, sierra_connection

logger = getLogger(__name__)


if __name__ == "__main__":
    tango: Database = tango_connection[config.db_name]
    sierra: Database = sierra_connection[config.db_name]

    alpha, beta, gamma = tango.alpha, tango.beta, sierra.gamma

    one_instance_times, two_instances_times = executor.execute(alpha, beta), executor.execute(alpha, gamma)

    logger.warning(f"1. One instance times = {one_instance_times}")
    logger.warning(f"2. Two instances times = {two_instances_times}")
