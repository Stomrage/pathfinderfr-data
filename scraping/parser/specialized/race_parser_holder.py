import re
from urllib import parse

from scraping.model.holder import Holder
from scraping.model.race import Race
from scraping.parser.parser_content import ParserContent
from scraping.parser.parser_for_holder import ParserForHolder
from scraping.util import data_util
from scraping.util.data_util import ComparisonMethod


class RaceParserHolder(ParserForHolder):
    race_name: str = None

    def create_data(self) -> Holder:
        return Race()

    def get_class_name(self):
        return self.race_name

    def __retrieve_racial_trait(self, trait_anchor):
        return {
            "name": trait_anchor.select_one("b").text.replace(".", "").strip(),
            "description": re.search("(?:[^.]+\.)(.*)", trait_anchor.text)[1].strip()
        }

    def parse_html(self, data_content: ParserContent):
        race_names = data_util.verify_race(parse.unquote(data_content.url).split(".")[3], ComparisonMethod.INSIDE)
        assert len(race_names) == 1
        self.race_name = race_names[0]
        race: Race = self._create_or_retrieve(self.race_name)
        race.race_name = self.race_name
        race.race_traits = list(map(lambda x: self.__retrieve_racial_trait(x), data_content.content.select("div.presentation > div > div > ul > li")))

    def parse_title(self, title_text):
        pass

    def parse_metadata(self, meta_text):
        pass
