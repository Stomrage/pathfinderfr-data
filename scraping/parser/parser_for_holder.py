from abc import ABC, abstractmethod
from typing import List

from scraping.model.holder import Holder
from scraping.parser.parser import Parser
from scraping.parser.parser_argument import ParserArgument


class ParserForHolder(Parser[Holder], ABC):

    def __init__(self, parser_arguments: List[ParserArgument]):
        super().__init__(parser_arguments)

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
