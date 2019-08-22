from model.talent import Talent
from parser.parser_holder import ParserHolder, ParserContent
from typing import Dict

from util import data_util
import libhtml
import re


class TalentParserHolder(ParserHolder):
    class_name: str = None
    talents_map: Dict[str, Talent] = {}

    @staticmethod
    def __normalize_talent_name(talent_name):
        talent_name = re.sub(r" \(.*\)\.?", "", talent_name)
        talent_name = talent_name.replace("-", " ")
        talent_name = talent_name.replace("’", "'")
        return talent_name

    def __create_or_retrieve(self, key):
        if key not in self.talents_map:
            talent = Talent()
            talent.class_name = self.class_name
            talent.talent_name = key
            self.talents_map[key] = talent
        return self.talents_map[key]

    def parse_title(self, title_text: str):
        class_name = (data_util.verify_class(title_text))
        if class_name is not None:
            self.class_name = class_name

    def parse_html(self, data_content: ParserContent):
        talents_description = data_content.content.select_one("div.article_2col")
        talent_name = None
        talent_text = None
        for talent_description in talents_description.children:
            if talent_description.name == "h3":
                if talent_name is not None:
                    self.__create_or_retrieve(talent_name).talent_description = talent_text
                talent_name = libhtml.cleanSectionName(talent_description.get_text())
                talent_name = self.__normalize_talent_name(talent_name)
                talent_text = ""
            elif talent_name is not None:
                talent_text += (libhtml.html2text(talent_description)).replace("\n", "")

        return list(self.talents_map.values())
