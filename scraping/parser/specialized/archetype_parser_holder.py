import re
import urllib
import urllib.parse

from scraping.main import libhtml
from scraping.model.archetype import Archetype
from scraping.model.holder import Holder
from scraping.parser.parser_content import ParserContent
from scraping.parser.parser_for_holder import ParserForHolder
from scraping.util import data_util


class ArchetypeParserHolder(ParserForHolder):

    def parse_metadata(self, meta_text):
        pass

    class_name: str = None
    archetype_name: str = None

    def get_class_name(self):
        return self.class_name

    def parse_html(self, data_content: ParserContent):
        archetype: Archetype = self._create_or_retrieve(self.archetype_name)
        class_name = data_util.verify_class(re.search("\((.*)\).ashx$", urllib.parse.unquote(data_content.url))[1])
        assert len(class_name) == 1
        archetype.class_name = class_name[0]
        archetype.archetype_name = self.archetype_name
        archetype.archetype_description = libhtml.cleanInlineDescription(
            data_content.content.select_one("#PageContentDiv > i").get_text()
        )

    def parse_title(self, title_text):
        title_search = re.search("([^()]*)(\(.*\))?", title_text)
        archetype_name = data_util.verify_archetype(title_search[1].strip())
        assert len(archetype_name) == 1
        self.archetype_name = archetype_name[0]

    def create_data(self) -> Holder:
        return Archetype()
