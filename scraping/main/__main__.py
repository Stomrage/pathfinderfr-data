import logging

from scraping.parser.parser_argument import ParserArgument
from scraping.parser.specialized.archetype_parser_argument import ArchetypeParserArgument
from scraping.parser.specialized.archetype_parser_holder import ArchetypeParserHolder
from scraping.parser.specialized.class_parser_holder import ClassParserHolder
from scraping.parser.specialized.talent_parser_holder import TalentParserHolder

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
    #
    # class_args = [
    #     ParserArgument(
    #         url="http://www.pathfinder-fr.org/Wiki/Pathfinder-RPG.Alchimiste.ashx", mock="classe-alchimiste.html"),
    #     ParserArgument(
    #         url="http://www.pathfinder-fr.org/Wiki/Pathfinder-RPG.Antipaladin.ashx", mock="classe-antipaladin.html"),
    #     ParserArgument(
    #         url="http://www.pathfinder-fr.org/Wiki/Pathfinder-RPG.Inquisiteur.ashx", mock="classe-inquisiteur.html"),
    #     ParserArgument(
    #         url="http://www.pathfinder-fr.org/Wiki/Pathfinder-RPG.Arpenteur%20dhorizon.ashx", mock="classe-arpenteur.html"),
    # ]
    # class_parser_holder = ClassParserHolder(class_args)
    # classes = class_parser_holder.run(use_mock=True)
    # data_accessor.save_yaml("new_classes.yaml", classes)
    archetype_args = [
        ParserArgument(url="http://www.pathfinder-fr.org/Wiki/Pathfinder-RPG.Les%20arch%C3%A9types%20de%20classes.ashx", mock="archetypes.html")
    ]
    archetype_parser_argument = ArchetypeParserArgument(archetype_args)
    archetypes = archetype_parser_argument.run(use_mock=True)
    # data_accessor.print_yaml(archetypes)


    mock_data = [
        ParserArgument(url="http://www.pathfinder-fr.org/Wiki/Pathfinder-RPG.Balafr%c3%a9%20enrag%c3%a9%20(barbare).ashx", mock="archetype-barbare-balafré.html"),
        ParserArgument(url="http://www.pathfinder-fr.org/Wiki/Pathfinder-RPG.Spirite%20hant%c3%a9%20(Spirite).ashx", mock="archetype-spirite-hanté.html"),
        ParserArgument(url="http://www.pathfinder-fr.org/Wiki/Pathfinder-RPG.Bretteur%20(roublard).ashx", mock="archetype-bretteur.html")
    ]
    archetype_parser_holder = ArchetypeParserHolder(mock_data)
    archetypes_holder = archetype_parser_holder.run(use_mock=True)
    data_accessor.save_yaml("new_archetypes.yaml", archetypes_holder)


