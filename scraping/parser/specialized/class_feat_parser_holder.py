import re

from scraping.parser.parser_content import ParserContent
from scraping.model.holder import Holder
from scraping.model.talent import Talent
from scraping.parser.parser_for_holder import ParserForHolder
from scraping.util import data_util
from scraping.main import libhtml


class ClassFeatParserHolder(ParserForHolder):

    class_name: str = None

    @staticmethod
    def __normalize_talent_name(talent_name):
        talent_name = re.sub(r" \(.*\)\.?", "", talent_name)
        talent_name = talent_name.replace("-", " ")
        talent_name = talent_name.replace("’", "'")
        return talent_name

    def create_data(self) -> Holder:
        return Talent()

    def parse_title(self, title_text: str):
        class_name = (data_util.verify_class(title_text))
        if class_name is not None:
            self.class_name = class_name

    def get_class_name(self):
        return self.class_name

    def parse_html(self, data_content: ParserContent):
        talents_description = data_content.content.select_one("div.article_2col")
        talent_name = None
        talent_text = None
        for talent_description in talents_description.children:
            if talent_description.name == "h3":
                if talent_name is not None:
                    self._create_or_retrieve(talent_name).talent_description = talent_text
                talent_name = libhtml.cleanSectionName(talent_description.get_text())
                talent_name = self.__normalize_talent_name(talent_name)
                talent_text = ""
            elif talent_name is not None:
                talent_text += (libhtml.html2text(talent_description)).replace("\n", "")
