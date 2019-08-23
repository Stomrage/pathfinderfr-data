import logging
from urllib import request
from abc import abstractmethod, ABC
from typing import List, TypeVar, Dict, Generic

from bs4 import BeautifulSoup

from scraping.main import libhtml
from scraping.mocks import mock_accessor
from scraping.parser.parser_argument import ParserArgument
from scraping.parser.parser_content import ParserContent

T = TypeVar("T")


class Parser(Generic[T], ABC):
    logger = logging.getLogger("PathfinderParser")
    PATHFINDER_FR_URL = "http://www.pathfinder-fr.org/Wiki/"
    data_map: Dict[str, Dict[str, T]]
    current_file: str = None

    def __init__(self, parser_arguments: List[ParserArgument]):
        self.parser_arguments = parser_arguments
        self.data_map = {}
        self.current_file = None

    def _create_or_retrieve(self, key):
        if self.current_file not in self.data_map:
            self.data_map[self.current_file] = {}
        current_map = self.data_map[self.current_file]
        if key not in current_map:
            holder = self.create_data()
            current_map[key] = holder
        return current_map[key]

    def retrieve_url(self, url):
        self.logger.debug("Accessing url : {url}".format(url=url))
        return request.urlopen(url).read()

    def __parse_arguments(self, use_mock):
        if use_mock:
            data_contents = [
                ParserContent(
                    url=parser_argument.url,
                    content=BeautifulSoup(mock_accessor.get_mock_file(parser_argument.mock), features="lxml").body
                )
                for parser_argument in
                list(filter(lambda parser_argument: parser_argument.has_mock(), self.parser_arguments))
            ]
        else:
            data_contents = [
                ParserContent(
                    url=parser_argument.url,
                    content=BeautifulSoup(self.retrieve_url(parser_argument.url), features="lxml").body
                )
                for parser_argument in self.parser_arguments
            ]
        return data_contents

    def run(self, use_mock=False):
        data_contents = self.__parse_arguments(use_mock)
        for data_content in data_contents:
            self.current_file = data_content.url
            self.parse_title(libhtml.cleanInlineDescription(data_content.content.select_one("h1.pagetitle").string))
            self.parse_html(data_content)
            self.abstract_run()

        flatten_holder = []
        for file_map in list(self.data_map.values()):
            flatten_holder.extend(list(file_map.values()))
        return flatten_holder

    @abstractmethod
    def parse_html(self, data_content: ParserContent):
        pass

    @abstractmethod
    def parse_title(self, title_text):
        pass

    @abstractmethod
    def create_data(self) -> T:
        pass

    @abstractmethod
    def abstract_run(self):
        pass
