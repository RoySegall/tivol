from django.test import TestCase
from tivol.base_classes.mappers import CsvMapper, YamlMapper, JsonMapper
from tivol.tests.assets.mappers_for_tests import DummyMapper
import os


class TestMappers(TestCase):
    """
    Testing mappers.
    """

    def test_set_destination_file(self):
        """
        Testing setting a single file for processing.
        """
        dummy_mapper = DummyMapper()
        dummy_mapper.set_destination_file('foo')

        self.assertEqual(dummy_mapper.source_type, 'file')
        self.assertEqual(dummy_mapper.source_path, 'foo')

    def test_set_destination_folder(self):
        """
        Testing setting a folder for processing.
        :return:
        """
        dummy_mapper = DummyMapper()
        dummy_mapper.set_destination_folder('foo')

        self.assertEqual(dummy_mapper.source_type, 'folder')
        self.assertEqual(dummy_mapper.source_path, 'foo')

    def parse_file(self, file, mapper, key=0):
        """
        Parsing a file and return the parsed content.

        :param file: The file to parse from the assets folder.
        :param mapper: The mapper to handle the file.
        :param key: Key to return. Default is 0. If set None will return all
            the object.

        :return: Parsed content.
        """
        path = os.path.join(
            os.getcwd(), 'tivol', 'tests', 'assets', file
        )

        mapper.set_destination_file(path=path)

        processed = mapper.process()
        if key is 0:
            return processed[0]
        return processed

    def test_csv_parser(self):
        """
        Testing the CSV file parser.
        """
        self.assertEqual(
            self.parse_file('animals.csv', CsvMapper()),
            {
                'id': 'animal_1',
                'animal_name': 'Cat',
                'sound': 'Meow',
                'number_of_legs': '4'
            }
        )

    def test_yaml_parser(self):
        """
        Testing the yaml file parsing.
        """
        first_row = {
            'id': 'company_1',
            'name': 'Apple',
            'description': 'Created the Mac, iPhone, iPad and more cool stuff',
            'founded_at': 'April 1, 1976',
            'founded_by': 'Steve Jobs, Steve Wozniak, Ronald Wayne'
        }
        self.assertEqual(self.parse_file('companies.yml', YamlMapper()),
                         first_row)

    def test_json_parser(self):
        """
        Testing the yaml file parsing.
        """
        first_row = {
            'birth_date': 'June 1, 1937',
            'id': 'actor_1',
            'name': 'Morgan Freeman'
        }
        self.assertEqual(self.parse_file('actors.json', JsonMapper()),
                         first_row)
