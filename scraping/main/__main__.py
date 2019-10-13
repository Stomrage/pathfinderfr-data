import logging

from scraping.parser.parser import MockOption

from scraping.parser.specialized.archetype_parser_argument import ArchetypeParserArgument
from scraping.parser.specialized.archetype_parser_holder import ArchetypeParserHolder
from scraping.parser.specialized.class_feat_parser_argument import ClassFeatParserArgument
from scraping.parser.specialized.class_parser_argument import ClassParserArgument
from scraping.parser.specialized.class_parser_holder import ClassParserHolder
from scraping.parser.specialized.class_feat_parser_holder import ClassFeatParserHolder
from scraping.parser.specialized.race_parser_argument import RaceParserArgument

from data import data_accessor
from scraping.parser.specialized.race_parser_holder import RaceParserHolder

#TODO change the process inside parser_for_holder to not use class_name as the main id field
# But instead use the id of the dataclass
if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO)

    race_parser_argument_args = [
        "https://www.pathfinder-fr.org/Wiki/Pathfinder-RPG.Races.ashx"
    ]
    race_parser_argument = RaceParserArgument(race_parser_argument_args)
    race_parser_holder_args = race_parser_argument.run(mock_option=MockOption.ONLY_MOCK)

    race_parser_holder = RaceParserHolder(race_parser_holder_args)
    races = race_parser_holder.run(mock_option=MockOption.ONLY_MOCK)
    data_accessor.save_yaml("new_races.yaml", races)

    # class_parser_argument_args = [
    #     "http://www.pathfinder-fr.org/Wiki/Pathfinder-RPG.Classes.ashx"
    # ]
    # class_parser_argument = ClassParserArgument(class_parser_argument_args)
    # class_parser_holder_args = class_parser_argument.run(mock_option=MockOption.ONLY_MOCK)
    #
    # class_feat_parser_argument = ClassFeatParserArgument(class_parser_holder_args)
    # class_feat_holder_args = class_feat_parser_argument.run(MockOption.ONLY_MOCK)
    #
    # class_feat_parser_holder = ClassFeatParserHolder(class_feat_holder_args)
    # talents = class_feat_parser_holder.run(mock_option=MockOption.ONLY_MOCK)
    # data_accessor.save_yaml("new_class_feats.yaml", talents)
    #
    # class_parser_holder = ClassParserHolder(class_parser_holder_args)
    # classes = class_parser_holder.run(mock_option=MockOption.ONLY_MOCK)
    # data_accessor.save_yaml("new_classes.yaml", classes)
    # #
    # archetype_parser_argument_args = [
    #     "http://www.pathfinder-fr.org/Wiki/Pathfinder-RPG.Les%20arch%C3%A9types%20de%20classes.ashx"
    # ]
    # archetype_parser_argument = ArchetypeParserArgument(archetype_parser_argument_args)
    # archetype_parser_holder_args = archetype_parser_argument.run(mock_option=MockOption.ONLY_MOCK)
    # archetype_parser_holder = ArchetypeParserHolder(archetype_parser_holder_args)
    # archetypes_holder = archetype_parser_holder.run(mock_option=MockOption.ONLY_MOCK)
    # data_accessor.save_yaml("new_archetypes.yaml", archetypes_holder)
