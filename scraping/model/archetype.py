from dataclasses import dataclass

from scraping.model.holder import Holder


@dataclass
class Archetype(Holder):
    def get_id(self):
        return self.archetype_name

    yaml_tag = "Archetype"
    archetype_description: str = None
    archetype_name: str = None
