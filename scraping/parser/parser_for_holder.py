from abc import ABC, abstractmethod
from typing import List

from scraping.model.holder import Holder
from scraping.parser.parser import Parser


class ParserForHolder(Parser[Holder], ABC):

    @abstractmethod
    def create_data(self) -> Holder:
        pass

    def _create_or_retrieve(self, key):
        if self.current_file not in self.data_map:
            self.data_map[self.current_file] = {}
        current_map = self.data_map[self.current_file]
        if key not in current_map:
            holder = self.create_data()
            current_map[key] = holder
        return current_map[key]

    def __init__(self, parser_urls: List):
        super().__init__(parser_urls)

    @abstractmethod
    def get_class_name(self):
        pass

    def abstract_run(self):
        self.__write_class_name()

    def __write_class_name(self):
        if self.current_file not in self.data_map:
            self.logger.warning("Couldn't find values for the file : {file_name}".format(file_name=self.current_file))
        elif self.get_class_name() is not None:
            for holder in self.data_map[self.current_file].values():
                holder.class_name = self.get_class_name()
