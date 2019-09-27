import re
from urllib import parse

from scraping.parser.parser_content import ParserContent
from scraping.parser.parser_for_argument import ParserForArgument


class ClassFeatParserArgument(ParserForArgument):

    def __retrieve_class_feat_link(self, class_feat_anchor):
        return class_feat_anchor["href"]

    def parse_html(self, data_content: ParserContent):
        filtered_anchor_link = filter(lambda archetype_link: archetype_link is not None,
                                      [self.__retrieve_class_feat_link(archetype_anchor)
                                       for archetype_anchor
                                       in data_content.select_and_filter_by_regex(
                                          "#PageContentDiv div.fright > b > i > a, #PageContentDiv div[style*='float:right'] > b > i > a",
                                          re.compile(".*(?:pouvoirs|talents|exploits).*", re.IGNORECASE))])
        for anchor_link in filtered_anchor_link:
            self.add_data(self.PATHFINDER_FR_URL + parse.quote(parse.unquote(anchor_link)))

    def parse_title(self, title_text):
        pass

    def abstract_run(self):
        pass
