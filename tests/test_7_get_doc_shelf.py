import unittest
from parameterized import parameterized
from app import get_doc_shelf

FIXTURES = [ 
    ('2207 876234', '1'), 
    ('11-2', '1'), 
    ('5455 028765', '1'), 
    ('10006', '2')
]

class TestFunctions(unittest.TestCase):

    def SetUp(self):
        print('method SetUp')

    def TearDown(self):
        print('method TearDown')

    @parameterized.expand(FIXTURES)
    def test_get_doc_shelf(self, user_doc_number, expected_result):
        result = get_doc_shelf(user_doc_number)
        self.assertEqual(expected_result, result)