import unittest
from parameterized import parameterized
from app import append_doc_to_shelf

FIXTURES = [ 
    ('311', '1', True),
    ('9-1 1', '2', True), 
    ('999', '4', True)
]

class TestFunctions(unittest.TestCase):

    def SetUp(self):
        print('method SetUp')

    def TearDown(self):
        print('method TearDown')

    @parameterized.expand(FIXTURES)
    def test_append_doc_to_shelf(self, doc_number, shelf_number, expected_result):
        result = append_doc_to_shelf(doc_number, shelf_number)
        self.assertEqual(expected_result, result)