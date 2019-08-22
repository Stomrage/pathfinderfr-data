from typing import List, Dict

from model.holder import Holder


class Classe(Holder):
    yaml_tag = u"Classe"
    classe_description: str = None
    competence_de_classe: List = None
    de_vie: str = None
    progress_list: List[Dict] = None
