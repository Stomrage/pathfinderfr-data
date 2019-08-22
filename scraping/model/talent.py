import yaml


class Talent(yaml.YAMLObject):
    yaml_tag = u"Talent"
    class_name: str = None
    talent_name: str = None
    talent_description: str = None
    talent_level: int = None
