from pathlib import Path
from typing import List

import logging
import yaml

logger = logging.getLogger("MockAccessor")


def save_yaml(file_name, datas: List):
    logger.debug("Writing yaml file : {file_name}".format(file_name=file_name))
    file_path = Path(__file__).parent.joinpath(file_name)
    if not file_path.exists():
        file_path.touch()
    file = file_path.open('w')
    yaml.dump_all(datas, default_flow_style=False, allow_unicode=True, stream=file)
