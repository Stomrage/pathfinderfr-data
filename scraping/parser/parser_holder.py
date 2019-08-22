from abc import ABC, abstractmethod
from typing import List
from bs4 import BeautifulSoup
from mocks import mock_accessor

import libhtml
import logging
import urllib.request


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

    @abstractmethod
    def parse_html(self, data_content: ParserContent):
        pass

    @abstractmethod
    def parse_title(self, title_text):
        pass

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

    def run(self, use_mock=False):
        data_contents = self.__parse_arguments(use_mock)
        data_holders = []
        for data_content in data_contents:
            self.parse_title(libhtml.cleanInlineDescription(data_content.content.select_one("h1.pagetitle").string))
            data_holders.extend(self.parse_html(data_content))
        return data_holders
