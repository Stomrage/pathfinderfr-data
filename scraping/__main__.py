import logging

from parser.parser_holder import ParserArgument
from parser.talent_parser_holder import TalentParserHolder

from data import data_accessor

if __name__ == "__main__":
    logging.basicConfig(level=logging.DEBUG)
    arguments = [
        ParserArgument(
            url="http://www.pathfinder-fr.org/Wiki/Pathfinder-RPG.talents.ashx", mock="roublard-talents.html"),
        ParserArgument(
            url="http://www.pathfinder-fr.org/Wiki/Pathfinder-RPG.Talents%20(enqu%C3%AAteur).ashx", mock="enqueteur-talents.html")
    ]
    talent_parser_holder = TalentParserHolder(arguments)
    talents = talent_parser_holder.run(use_mock=True)
    data_accessor.save_yaml("talents.yaml", talents)    # print(*talents)
