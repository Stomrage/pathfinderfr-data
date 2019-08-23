import logging

from scraping.parser.class_parser_holder import ClassParserHolder
from scraping.parser.parser_holder import ParserArgument
from scraping.parser.talent_parser_holder import TalentParserHolder

from data import data_accessor

if __name__ == "__main__":
    logging.basicConfig(level=logging.DEBUG)
    # talent_args = [
    #     ParserArgument(
    #         url="http://www.pathfinder-fr.org/Wiki/Pathfinder-RPG.talents.ashx", mock="roublard-talents.html"),
    #     ParserArgument(
    #         url="http://www.pathfinder-fr.org/Wiki/Pathfinder-RPG.Talents%20(enqu%C3%AAteur).ashx", mock="enqueteur-talents.html")
    # ]
    # talent_parser_holder = TalentParserHolder(talent_args)
    # talents = talent_parser_holder.run(use_mock=True)
    # data_accessor.save_yaml("new_talents.yaml", talents)
    # print(*talents)

    class_args = [
        ParserArgument(
            url="http://www.pathfinder-fr.org/Wiki/Pathfinder-RPG.Alchimiste.ashx", mock="classe-alchimiste.html"),
        ParserArgument(
            url="http://www.pathfinder-fr.org/Wiki/Pathfinder-RPG.Antipaladin.ashx", mock="classe-antipaladin.html"),
        ParserArgument(
            url="http://www.pathfinder-fr.org/Wiki/Pathfinder-RPG.Inquisiteur.ashx", mock="classe-inquisiteur.html"),
        ParserArgument(
            url="http://www.pathfinder-fr.org/Wiki/Pathfinder-RPG.Arpenteur%20dhorizon.ashx", mock="classe-arpenteur.html"),
    ]
    class_parser_holder = ClassParserHolder(class_args)
    classes = class_parser_holder.run(use_mock=True)
    data_accessor.save_yaml("new_classes.yaml", classes)
