import logging
import os
from datetime import datetime


def get_meta() -> None:
    """
        get metadata from a file
    """
    stats = os.stat(("zen_of_python.txt"))
    logging.info(stats)
    # Size of the file
    logging.info(f"Size of the file: {stats.st_size}")
    # Last modified time
    logging.info(
        f"Date file was last modified: {datetime.fromtimestamp(stats.st_mtime)}"
    )
    # Last accessed time
    logging.info(
        f"Date file was last accessed: {datetime.fromtimestamp(stats.st_atime)}"
    )


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO, format="%(message)s")
    get_meta()
