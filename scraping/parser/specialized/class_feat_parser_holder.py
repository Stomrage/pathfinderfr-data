import re
from typing import List

from bs4 import BeautifulSoup

from scraping.parser.parser_content import ParserContent
from scraping.model.holder import Holder
from scraping.model.classfeat import ClassFeat
from scraping.parser.parser_for_holder import ParserForHolder
from scraping.util import data_util
from scraping.main import libhtml
from scraping.util.data_util import ComparisonMethod


class ClassFeatParserHolder(ParserForHolder):
    class_name: str = None

    def create_data(self) -> Holder:
        return ClassFeat()

    def parse_title(self, title_text: str):
        class_name = (data_util.verify_class(title_text, ComparisonMethod.INSIDE))
        if class_name is not None:
            self.class_name = class_name

    def get_class_name(self):
        return self.class_name

    def parse_html(self, data_content: ParserContent):
        class_feat_map = data_content.select_and_extract_text_until(selector="h3.separator", tag_name="h3")
        for class_feat_key in class_feat_map.keys():
            class_feat: ClassFeat = self._create_or_retrieve(class_feat_key)
            class_feat.class_name = self.class_name
            class_feat.class_feat_description = class_feat_map[class_feat_key]
