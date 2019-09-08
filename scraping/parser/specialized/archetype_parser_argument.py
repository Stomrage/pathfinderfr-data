import re

from scraping.parser.parser_content import ParserContent
from scraping.parser.parser_for_argument import ParserForArgument


class ArchetypeParserArgument(ParserForArgument):

    def __retrieve_archetype_link(self, archetype_list_anchor):
        archetype_link = archetype_list_anchor["href"]
        if re.search(r"\([a-zA-Z%0-9]+\)\.ashx$", archetype_link):
            return archetype_link
        else:
            return None

    def parse_html(self, data_content: ParserContent):
        filtered_anchor_link = filter(lambda archetype_link: archetype_link is not None,
               [self.__retrieve_archetype_link(archetype_anchor)
                for archetype_anchor
                in data_content.content.select("div.presentation.navmenudroite > ul > li > a")])
        for anchor_link in filtered_anchor_link:
            self.add_data(self.PATHFINDER_FR_URL+anchor_link)

    def parse_title(self, title_text):
        pass
        # print(title_text)

    def abstract_run(self):
        pass