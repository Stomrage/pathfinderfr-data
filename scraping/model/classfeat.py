from dataclasses import dataclass

from scraping.model.holder import Holder


@dataclass
class ClassFeat(Holder):
    def get_id(self):
        return self.class_feat_name

    yaml_tag = u"ClassFeat"
    class_feat_name: str = None
    class_feat_description: str = None
    class_feat_level: int = None
