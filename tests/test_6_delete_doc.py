import unittest
from parameterized import parameterized
from app import delete_doc

FIXTURES = [
    ('2207 876234', True), 
    ('11-2', True), 
    ('10006', True)
]

class TestFunctions(unittest.TestCase):

    def SetUp(self):
        print('method SetUp')

    def TearDown(self):
        print('method TearDown')

    @parameterized.expand(FIXTURES)
    def test_delete_doc(self, doc_number, expected_result):
        result = delete_doc(doc_number)
        self.assertEqual(expected_result, result)