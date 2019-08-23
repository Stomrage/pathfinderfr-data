from scraping.model.holder import Holder


class Talent(Holder):
    yaml_tag = u"Talent"
    talent_name: str = None
    talent_description: str = None
    talent_level: int = None
