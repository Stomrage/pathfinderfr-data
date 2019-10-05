import re
from functools import reduce

from typing import Pattern, List
from bs4 import BeautifulSoup

from scraping.main import libhtml


class ParserContent:
    def __init__(self, url: str, content: BeautifulSoup):
        self.url = url
        self.content = content

    def select_and_filter_one_by_regex(self, selector: str, regex: Pattern) -> BeautifulSoup:
        filter_results = self.select_and_filter_by_regex(selector, regex)
        assert (len(filter_results) == 1)
        return filter_results[0]

    def select_and_filter_by_regex(self, selector: str, regex: Pattern) -> List:
        return list(filter(lambda x: regex.match(x.text), self.content.select(selector)))

    def select_and_extract_text_until(self, selector: str, tag_name: str):
        selected_map = {}
        for selected_bs in self.content.select(selector):
            selected_map[self.__clean_title(selected_bs.text)] = reduce(lambda a,b: a+libhtml.html2text(b).replace("\n", ""), self.__extract_siblings_until_tag(tag_name, selected_bs), "")
        return selected_map

    @staticmethod
    def __clean_title(title_text: str):
        return re.sub("¶|\.|\*|\(Ext\)|\(Sur\)|\(Mag\)", "", title_text).strip()

    @staticmethod
    def __extract_siblings_until_tag(tag_name: str, current_bs: BeautifulSoup):
        extracted_siblings = []
        for sibling in current_bs.next_siblings:
            if sibling.name == tag_name:
                break
            extracted_siblings.append(sibling)
        return extracted_siblings
