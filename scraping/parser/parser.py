import html
import logging
from urllib import request, parse
from abc import abstractmethod, ABC
from typing import List, TypeVar, Dict, Generic

from bs4 import BeautifulSoup

from scraping.main import libhtml
from scraping.mocks import mock_accessor
from scraping.parser.parser_content import ParserContent

from enum import Enum


class MockOption(Enum):
    UPDATE_MOCK = 1
    NO_MOCK = 2
    ONLY_MOCK = 3


T = TypeVar("T")


class Parser(Generic[T], ABC):
    PATHFINDER_FR_URL = "http://www.pathfinder-fr.org/Wiki/"
    data_map: Dict[str, Dict[str, T]]
    current_file: str = None

    def __init__(self, parser_urls: List[str]):
        self.logger = logging.getLogger(self.__class__.__name__)
        self.parser_urls = parser_urls
        self.data_map = {}
        self.current_file = None

    def retrieve_url(self, url):
        self.logger.debug("Accessing url : {url}".format(url=url))
        return request.urlopen(url).read()

    def __parse_arguments(self, mock_option):
        for parser_argument in self.parser_urls:
            if mock_option == MockOption.ONLY_MOCK:
                self.__run_one(ParserContent(
                    url=parser_argument,
                    content=BeautifulSoup(mock_accessor.get_mock_file(holder=self.__class__.__name__, filename=parser_argument), features="lxml").body
                ))
            elif mock_option == MockOption.NO_MOCK:
                self.__run_one(ParserContent(
                    url=parser_argument,
                    content=BeautifulSoup(self.retrieve_url(parser_argument), features="lxml").body
                ))
            elif mock_option == MockOption.UPDATE_MOCK:
                mock_accessor.creat_mock_file(holder=self.__class__.__name__, filename=parser_argument, data=self.retrieve_url(parser_argument))

    def __run_one(self, data_content):
        self.logger.debug("Parsing data from : {url}".format(url=data_content.url))
        self.current_file = data_content.url
        self.parse_title(libhtml.cleanInlineDescription(data_content.content.select_one("h1.pagetitle").string))
        self.parse_html(data_content)
        self.abstract_run()

    def run(self, mock_option: MockOption = MockOption.ONLY_MOCK):
        self.__parse_arguments(mock_option=mock_option)
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
    def abstract_run(self):
        pass
