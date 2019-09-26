from pathlib import Path

import re
import logging

logger = logging.getLogger("MockAccessor")

normalize_regex: str = r"^https?://www.pathfinder-fr.org/Wiki/(.*)\.ashx"


def __normalize_filename(filename):
    regex_result = re.match(normalize_regex, filename)
    if regex_result:
        return regex_result.group(1)
    else:
        return filename


def get_mock_file(holder: str, filename: str):
    logger.debug("Accessing mocking file : {filename}".format(filename=filename))
    holder_path = Path(__file__).parent.joinpath(holder)
    return str(holder_path.joinpath(__normalize_filename(filename)).open(encoding="utf-8").read())


def create_mock_file(holder: str, filename: str, data: str):
    logger.debug("Creating mocking file : {filename}".format(filename=filename))
    holder_path = Path(__file__).parent.joinpath(holder)
    if not holder_path.exists():
        holder_path.mkdir()
    holder_path.joinpath(__normalize_filename(filename)).open(mode="w+b").write(data)
