from logging import getLogger

from pymongo.database import Database

from algorithms import ex_one
from config import config
from connector import connection

from algorithms.utils import fill_collection

logger = getLogger(__name__)


if __name__ == "__main__":
    database: Database = connection[config.db_name]

    alpha = database.alpha
    beta = database.beta

    logger.warning(f"ALPHA = {alpha}")
    logger.warning(f"BETA = {beta}")

    fill_collection(alpha)
    logger.warning(f"COUNT = {alpha.count_documents()}")

