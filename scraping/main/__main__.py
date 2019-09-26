import logging

from scraping.parser.parser import MockOption

from scraping.parser.specialized.archetype_parser_argument import ArchetypeParserArgument
from scraping.parser.specialized.archetype_parser_holder import ArchetypeParserHolder
from scraping.parser.specialized.class_parser_argument import ClassParserArgument
from scraping.parser.specialized.class_parser_holder import ClassParserHolder
from scraping.parser.specialized.talent_parser_holder import TalentParserHolder

from data import data_accessor

if __name__ == "__main__":
    logging.basicConfig(level=logging.DEBUG)
    # talent_parser_holder_args = [
    #         "http://www.pathfinder-fr.org/Wiki/Pathfinder-RPG.talents.ashx",
    #         "http://www.pathfinder-fr.org/Wiki/Pathfinder-RPG.Talents%20(enqu%C3%AAteur).ashx"
    # ]
    # talent_parser_holder = TalentParserHolder(talent_parser_holder_args)
    # talents = talent_parser_holder.run(mock_option=MockOption.ONLY_MOCK)
    # data_accessor.save_yaml("new_talents.yaml", talents)

    class_parser_argument_args = [
        "http://www.pathfinder-fr.org/Wiki/Pathfinder-RPG.Classes.ashx"
    ]
    class_parser_argument = ClassParserArgument(class_parser_argument_args)
    class_parser_holder_args = class_parser_argument.run(mock_option=MockOption.ONLY_MOCK)
    # class_parser_holder_args = [
    #     " http://www.pathfinder-fr.org/Wiki/Pathfinder-RPG.Prêtre.ashx"
    # ]
    class_parser_holder = ClassParserHolder(class_parser_holder_args)
    classes = class_parser_holder.run(mock_option=MockOption.ONLY_MOCK)
    data_accessor.save_yaml("new_classes.yaml", classes)

    # archetype_parser_argument_args = [
    #     "http://www.pathfinder-fr.org/Wiki/Pathfinder-RPG.Les%20arch%C3%A9types%20de%20classes.ashx"
    # ]
    # archetype_parser_argument = ArchetypeParserArgument(archetype_parser_argument_args)
    # archetype_parser_holder_args = archetype_parser_argument.run(mock_option=MockOption.ONLY_MOCK)
    # archetype_parser_holder = ArchetypeParserHolder(archetype_parser_holder_args)
    # archetypes_holder = archetype_parser_holder.run(mock_option=MockOption.ONLY_MOCK)
    # data_accessor.save_yaml("new_archetypes.yaml", archetypes_holder)


