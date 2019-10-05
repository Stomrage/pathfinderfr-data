from pathlib import Path
from typing import List

import logging
import yaml

logger = logging.getLogger("MockAccessor")


def get_data_file(filename: str):
    logger.debug("Accessing data file : {filename}".format(filename=filename))
    holder_path = Path(__file__).parent
    return str(holder_path.joinpath(filename).open(encoding="utf-8").read())


def save_yaml(file_name, datas: List):
    if datas:
        logger.debug("Writing yaml file : {file_name}".format(file_name=file_name))
        file_path = Path(__file__).parent.joinpath(file_name)
        if not file_path.exists():
            file_path.touch()
        file = file_path.open('w', encoding="utf-8")
        yaml.dump_all(datas, default_flow_style=False, allow_unicode=True, stream=file, encoding="utf-8")
    else:
        logger.debug("Nothing to write : {file_name}".format(file_name=file_name))


def print_yaml(datas: List):
    print(yaml.dump_all(datas, default_flow_style=False, allow_unicode=True))
