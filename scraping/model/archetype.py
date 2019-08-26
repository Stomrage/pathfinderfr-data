from scraping.model.holder import Holder


class Archetype(Holder):
    yaml_tag = "Archetype"
    archetype_description: str = None
    archetype_name: str = None
