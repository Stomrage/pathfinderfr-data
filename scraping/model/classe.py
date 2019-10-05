from typing import List, Dict

from scraping.model.holder import Holder
from dataclasses import dataclass


@dataclass
class Classe(Holder):
    def get_id(self):
        return self.class_name

    yaml_tag = u"Classe"
    classe_description: str = None
    competence_de_classe: List = None
    de_vie: str = None
    progress_list: List[Dict] = None
