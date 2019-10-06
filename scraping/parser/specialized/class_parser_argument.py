import re
from urllib import parse

from scraping.parser.parser_content import ParserContent
from scraping.parser.parser_for_argument import ParserForArgument


class ClassParserArgument(ParserForArgument):

    def parse_title(self, title_text):
        pass

    def abstract_run(self):
        pass

    def parse_metadata(self, meta_text):
        pass

    def __retrieve_class_link(self, class_list_anchor):
        class_search = re.search("\.?/?(.*)", class_list_anchor["href"])
        return class_search[1]

    def parse_html(self, data_content: ParserContent):
        filtered_anchor_link = filter(lambda archetype_link: archetype_link is not None,
                                      [self.__retrieve_class_link(archetype_anchor)
                                       for archetype_anchor
                                       in data_content.content.select(
                                          "div.presentation.navmenu:has(>h2.separator:not(:contains('occultes'))) > table > tr > center > table > tr > td > a")])
        for anchor_link in filtered_anchor_link:
            self.add_data(self.PATHFINDER_FR_URL + parse.quote(parse.unquote(anchor_link)))