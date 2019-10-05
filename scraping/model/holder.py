from abc import abstractmethod, ABC

import yaml


class Holder(yaml.YAMLObject):
    yaml_loader = yaml.SafeLoader
    class_name: str = None

    def __hash__(self):
        return hash(self.get_id())

    @abstractmethod
    def get_id(self):
        pass
