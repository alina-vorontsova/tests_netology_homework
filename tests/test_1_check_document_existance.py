import unittest
from parameterized import parameterized
from app import check_document_existance


FIXTURES = [
    ('2207 876234', True), 
    ('11-2', True), 
    ('10006', True),
    ('101', False),
    ('333', False),
    ('9 9-1', False)
]

class TestFunctions(unittest.TestCase):

    def SetUp(self):
        print('method SetUp')

    def TearDown(self):
        print('method TearDown')

    @parameterized.expand(FIXTURES)
    def test_check_document_existance(self, doc_number, expected_result):
        result = check_document_existance(doc_number)
        self.assertEqual(expected_result, result)