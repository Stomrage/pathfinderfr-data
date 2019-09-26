import re

from typing import Pattern
from bs4 import BeautifulSoup


class ParserContent:
    def __init__(self, url: str, content: BeautifulSoup):
        self.url = url
        self.content = content

    def select_and_filter_one_by_regex(self, selector: str, regex: Pattern) -> BeautifulSoup:
        filter_results = self.select_and_filter_by_regex(selector, regex)
        assert(len(filter_results) == 1)
        return filter_results[0]

    def select_and_filter_by_regex(self, selector: str, regex: Pattern) -> list:
        return list(filter(lambda x: regex.match(x.text), self.content.select(selector)))
