from pathlib import Path

import logging

logger = logging.getLogger("MockAccessor")


def get_mock_file(file_name):
    logger.debug("Accessing mocking file : {file_name}".format(file_name=file_name))
    return str((Path(__file__).parent.joinpath(file_name)).open().read())
