from abc import ABC
from typing import List

from scraping.parser.parser import Parser
from scraping.parser.parser_argument import ParserArgument


class ParserForArgument(Parser[ParserArgument], ABC):

    def __init__(self, parser_arguments: List[ParserArgument]):
        super().__init__(parser_arguments)

    def create_data(self) -> ParserArgument:
        return ParserArgument()
