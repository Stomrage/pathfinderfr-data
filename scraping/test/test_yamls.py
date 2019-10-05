import unittest
from typing import List, Dict

import yaml

from data import data_accessor
from scraping.model.archetype import Archetype
from scraping.model.classe import Classe
from scraping.model.classfeat import ClassFeat

from scraping.test.resources import resource_accessor


class TestYamls(unittest.TestCase):
    expected_classes_yaml = resource_accessor.get_resource_file("classes.yaml")
    actual_classes_yaml = data_accessor.get_data_file("new_classes.yaml")

    expected_class_feats_yaml = resource_accessor.get_resource_file("class_feats.yaml")
    actual_class_feats_yaml = data_accessor.get_data_file("new_class_feats.yaml")

    expected_archetypes_yaml = resource_accessor.get_resource_file("archetypes.yaml")
    actual_archetypes_yaml = data_accessor.get_data_file("new_archetypes.yaml")

    def test_classes(self):
        excepted_classes: Dict[int, Classe] = dict(
            map(lambda x: (x.get_id(), x), yaml.safe_load_all(self.expected_classes_yaml)))
        actual_classes: Dict[int, Classe] = dict(
            map(lambda x: (x.get_id(), x), yaml.safe_load_all(self.actual_classes_yaml)))
        self.assertListEqual(list(excepted_classes.keys()), list(actual_classes.keys()))
        self.assertDictEqual(excepted_classes, actual_classes)

    def test_classfeats(self):
        excepted_class_feats: Dict[int, ClassFeat] = dict(
            map(lambda x: (x.get_id(), x), yaml.safe_load_all(self.expected_class_feats_yaml)))
        actual_class_feats: Dict[int, ClassFeat] = dict(
            map(lambda x: (x.get_id(), x), yaml.safe_load_all(self.actual_class_feats_yaml)))
        self.assertListEqual(list(excepted_class_feats.keys()), list(actual_class_feats.keys()))
        self.assertDictEqual(excepted_class_feats, actual_class_feats)

    def test_archetypes(self):
        excepted_archetypes: Dict[int, Archetype] = dict(
            map(lambda x: (x.get_id(), x), yaml.safe_load_all(self.expected_archetypes_yaml)))
        actual_archetypes: Dict[int, Archetype] = dict(
            map(lambda x: (x.get_id(), x), yaml.safe_load_all(self.actual_archetypes_yaml)))
        self.assertListEqual(list(excepted_archetypes.keys()), list(actual_archetypes.keys()))
        self.assertDictEqual(excepted_archetypes, actual_archetypes)

