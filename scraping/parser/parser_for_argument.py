from abc import ABC

from scraping.parser.parser import Parser
from scraping.parser.parser_argument import ParserArgument


class ParserForArgument(Parser[ParserArgument], ABC):
    def create_data(self) -> ParserArgument:
        return ParserArgument()
