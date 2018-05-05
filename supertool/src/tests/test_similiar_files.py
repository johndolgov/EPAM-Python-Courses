from io import StringIO
from tempfile import TemporaryDirectory
import os
import unittest
from unittest.mock import patch

from supertool import simfiles_finder


def create_file(file_path, text):

    with open(file_path, 'w') as file:
        file.write(text)


class TestForGetHash(unittest.TestCase):
    """
    This class for testing get_hash function
    """

    def pattern_with_creation_temp_file_and_get_hash(self, text, expected_hash):

        with TemporaryDirectory() as temp_dir:
            file_path = os.path.join(temp_dir, 'tmp')
            create_file(file_path, text)
            self.assertEqual(expected_hash,
                             simfiles_finder.get_hash(file_path))

    def test_get_hash_from_empty_file(self):

        self.pattern_with_creation_temp_file_and_get_hash('',
                                            'd41d8cd98f00b204e9800998ecf8427e')

    def test_get_hash_from_full_file(self):

        self.pattern_with_creation_temp_file_and_get_hash('111',
                                            '698d51a19d8a121ce581499d7b701668')


class TestForDuplicateFinder(unittest.TestCase):
    """
    This class for test check_for_duplicates function
    """

    @staticmethod
    def not_unique_files_in_directory(path):
        text = '12345'
        not_unique_dict = {}
        for i in range(2):
            file_path = os.path.join(path, 'file' + str(i))
            create_file(file_path, text)
            if not_unique_dict.get((simfiles_finder.get_hash(file_path))):
               not_unique_dict[(simfiles_finder.get_hash(file_path))].append(file_path)
            else:
               not_unique_dict[(simfiles_finder.get_hash(file_path))] = []
               not_unique_dict[(simfiles_finder.get_hash(file_path))].append(file_path)

        return not_unique_dict

    @staticmethod
    def unique_files_in_the_directory(path):
        text_1 = '1234'
        text_2 = '45678'
        file_path = os.path.join(path, 'file21')
        create_file(file_path, text_1)
        file_path = os.path.join(path, 'file22')
        create_file(file_path, text_2)

    def test_for_not_existing_directory(self):
        with self.assertRaises(ValueError) as raised_exception:
            simfiles_finder.check_for_duplicates('M:\\NotExist')
        self.assertEqual(raised_exception.exception.args[0], "Directory do not exist")

    def test_for_not_unique_files(self):
        with TemporaryDirectory() as temp_dir:
            self.not_unique_files_in_directory(temp_dir)

    def test_for_unique_files(self):
        with TemporaryDirectory() as temp_dir:
            not_unique_dict = self.not_unique_files_in_directory(temp_dir)
            not_unique_list = set((k, tuple(sorted(v)))
                                       for k, v, in not_unique_dict.items())
            result = set((k, tuple(sorted(v))) for k, v, in simfiles_finder.check_for_duplicates(temp_dir).items())

            self.assertSetEqual(not_unique_list, result)

    def test_duplicates_printer_unique_files(self):

        with patch('sys.stdout', new=StringIO()) as fake_out:
            with TemporaryDirectory() as temp_dir:
                file_path1 = os.path.join(temp_dir, 'file1')
                create_file(file_path1, '12345')

                another_dir = os.path.join(temp_dir, 'file2')
                os.makedirs(another_dir)
                file_path2 = os.path.join(another_dir, 'file2')
                create_file(file_path2, '12345')

                simfiles_finder.printer(simfiles_finder.check_for_duplicates(temp_dir))
                output = 'There is duplicate:\n-------------------\n\n' \
                         'This files duplicate each other\n------------------\n\n'
                output += file_path1 + '\nand\n'
                output += file_path2
            self.assertEqual(fake_out.getvalue().strip(), output)

    def test_duplicates_printer_non_unique_files(self):

        with patch('sys.stdout', new=StringIO()) as fake_out:
            with TemporaryDirectory() as temp_dir:
                file_path1 = os.path.join(temp_dir, 'file1')
                create_file(file_path1, '12345')

                another_dir = os.path.join(temp_dir, 'file2')
                os.makedirs(another_dir)
                file_path2 = os.path.join(another_dir, 'file2')
                create_file(file_path2, '123456')

                simfiles_finder.printer(simfiles_finder.check_for_duplicates(temp_dir))
                output = 'There is not duplicates here'
            self.assertEqual(fake_out.getvalue().strip(), output)











