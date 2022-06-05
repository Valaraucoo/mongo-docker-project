from logging import getLogger

from connector import connection

logger = getLogger(__name__)

if __name__ == "__main__":
    logger.warning(f"Connection status: {connection}")
