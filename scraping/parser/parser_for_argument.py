from abc import ABC
from typing import List

from scraping.parser.parser import Parser


class ParserForArgument(Parser[str], ABC):

    def __init__(self, parser_urls: List):
        super().__init__(parser_urls)

    def add_data(self, url):
        if self.current_file not in self.data_map:
            self.data_map[self.current_file] = {}
        current_map = self.data_map[self.current_file]
        current_map[url] = url
