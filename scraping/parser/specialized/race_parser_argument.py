import re
from urllib import parse

from scraping.parser.parser_content import ParserContent
from scraping.parser.parser_for_argument import ParserForArgument


class RaceParserArgument(ParserForArgument):

    def __retrieve_race_link(self, class_list_anchor):
        class_search = re.search("\.?/?(.*)", class_list_anchor["href"])
        return class_search[1]

    def parse_html(self, data_content: ParserContent):
        filtered_anchor_link = filter(lambda race_link: race_link is not None,
                                      [self.__retrieve_race_link(race_anchor)
                                       for race_anchor
                                       in data_content.content.select(
                                          "div.presentation.navmenu tr > td > a.pagelink")])
        for anchor_link in filtered_anchor_link:
            self.add_data(self.PATHFINDER_FR_URL + parse.quote(parse.unquote(anchor_link)))

    def parse_title(self, title_text):
        pass

    def abstract_run(self):
        pass

    def parse_metadata(self, meta_text):
        pass
