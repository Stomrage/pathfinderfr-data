import logging
from pathlib import Path

logger = logging.getLogger("MockAccessor")


def get_resource_file(filename: str):
    logger.debug("Accessing resource file : {filename}".format(filename=filename))
    holder_path = Path(__file__).parent
    return str(holder_path.joinpath(filename).open(encoding="utf-8").read())
