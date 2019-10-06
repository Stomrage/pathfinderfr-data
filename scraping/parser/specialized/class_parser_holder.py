from typing import Dict

import re

from scraping.parser.parser_content import ParserContent
from scraping.main import libhtml
from scraping.parser.parser_for_holder import ParserForHolder
from scraping.model.classe import Classe
from scraping.model.holder import Holder
from scraping.util import data_util


class ClassParserHolder(ParserForHolder):
    def parse_metadata(self, meta_text):
        pass

    class_name: str = None

    def create_data(self) -> Holder:
        return Classe()

    def get_class_name(self):
        return self.class_name

    @staticmethod
    def __retrieve_competence_text(competences_anchor):
        competence_string = ""
        next_element = competences_anchor.find_next(string=True)
        while next_element:
            competence_string += next_element
            next_sibling = next_element.find_next_sibling()
            if next_sibling is not None:
                if next_sibling.name == "br":
                    break
            next_element = next_element.find_next(string=True)
        return competence_string

    def __retrieve_de_vie(self, de_vie_anchor):
        return de_vie_anchor.find_next(string=True).find_next(string=True).replace(".", "").strip()

    def __retrieve_progress(self, progress_table_anchor):
        progress_list = []
        for tr in progress_table_anchor.select("tr:not(.soustitre, .titre, .note)"):
            tds = tr.select("td:not(.note)", limit=5)
            if tds:
                row = [i.text for i in tds]
                progress_list.append({
                    "Niveau": int(row[0]),
                    "BBA": row[1],
                    "Réflexes": row[2],
                    "Vigueur": row[3],
                    "Volonté": row[4]
                })
        return progress_list

    def parse_html(self, data_content: ParserContent):
        classe: Classe = self._create_or_retrieve(self.class_name)
        classe.classe_description = \
            (libhtml.html2text(data_content.content.select_one("#PageContentDiv > i"))).replace("\n", "")
        competence_string = self.__retrieve_competence_text(
            data_content.select_and_filter_one_by_regex("h2.separator", re.compile(".*Compétences.*", flags=re.IGNORECASE)))
        classe.competence_de_classe = data_util.verify_competence(competence_string)
        classe.de_vie = self.__retrieve_de_vie(
            data_content.content.select_one("b:contains('Dés de vie'), b:contains('Dé de vie')"))
        classe.progress_list = self.__retrieve_progress(data_content.content.select_one("table.tablo"))

    def parse_title(self, title_text):
        class_name = (data_util.verify_class(title_text))
        assert len(class_name) == 1
        class_name = class_name[0]
        if class_name is not None:
            self.class_name = class_name
