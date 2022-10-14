import unittest
from parameterized import parameterized
from app import remove_doc_from_shelf, directories

FIXTURES = [ 
    ('2207 876234', False), 
    ('11-2', False),
    ('10006', False)
]

class TestFunctions(unittest.TestCase):

    def SetUp(self):
        print('method SetUp')

    def TearDown(self):
        print('method TearDown')

    @parameterized.expand(FIXTURES)
    def test_remove_doc_from_shelf(self, doc_number, expected_result):
        remove_doc_from_shelf(doc_number)
        result = self.check_document(doc_number)
        self.assertEqual(expected_result, result)

    def check_document(self, doc_number):
        """Проверка, удалился ли документ с полки."""
        doc_founded = False
        for directory_number, directory_docs_list in directories.items():
            if doc_number in directory_docs_list:
                doc_founded = True
                break
        return doc_founded