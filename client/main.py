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

    logger.warning(f"1. Times = {executor.execute(alpha, beta, num_iteration=300, step=20)}")
    logger.warning(f"2. Times = {executor.execute(alpha, gamma, num_iteration=300, step=20)}")
