from typing import List, Dict

from dataclasses import dataclass
from scraping.model.holder import Holder


@dataclass
class Race(Holder):
    yaml_tag = u"Race"

    race_name: str = None
    race_traits: List[Dict] = None

    def get_id(self):
        return self.race_name
