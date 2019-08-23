from abc import ABC, abstractmethod
from typing import List, Dict
from bs4 import BeautifulSoup
import logging
import urllib.request

from scraping.mocks import mock_accessor
from scraping.main import libhtml
from scraping.model.holder import Holder


class ParserContent:
    def __init__(self, url: str, content: BeautifulSoup):
        self.url = url
        self.content = content


class ParserArgument:
    def __init__(self, url: str, mock: str = None):
        self.url = url
        self.mock = mock

    def has_mock(self):
        return self.mock is not None


class ParserHolder(ABC):
    logger = logging.getLogger("PathfinderParser")
    holders_map: Dict[str, Dict[str, Holder]] = {}
    current_file: str = None

    @abstractmethod
    def parse_html(self, data_content: ParserContent):
        pass

    @abstractmethod
    def parse_title(self, title_text):
        pass

    @abstractmethod
    def generate_holder(self) -> Holder:
        pass

    @abstractmethod
    def get_class_name(self):
        pass

    def _create_or_retrieve(self, key):
        if self.current_file not in self.holders_map:
            self.holders_map[self.current_file] = {}
        current_map = self.holders_map[self.current_file]
        if key not in current_map:
            holder = self.generate_holder()
            current_map[key] = holder
        return current_map[key]

    def __init__(self, parser_arguments: List[ParserArgument]):
        self.parser_arguments = parser_arguments

    def retrieve_url(self, url):
        self.logger.debug("Accessing url : {url}".format(url=url))
        return urllib.request.urlopen(url).read()

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

    def __write_class_name(self):
        if self.current_file not in self.holders_map:
            self.logger.warning("Couldn't find values for the file : {file_name}".format(file_name=self.current_file))
        else:
            for holder in self.holders_map[self.current_file].values():
                holder.class_name = self.get_class_name()

    def run(self, use_mock=False):
        data_contents = self.__parse_arguments(use_mock)
        for data_content in data_contents:
            self.current_file = data_content.url
            self.parse_title(libhtml.cleanInlineDescription(data_content.content.select_one("h1.pagetitle").string))
            self.parse_html(data_content)
            self.__write_class_name()

        flatten_holder = []
        for file_map in list(self.holders_map.values()):
            flatten_holder.extend(list(file_map.values()))
        return flatten_holder
