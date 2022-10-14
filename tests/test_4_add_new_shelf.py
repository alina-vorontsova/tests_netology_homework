import unittest
from parameterized import parameterized
from app import add_new_shelf

FIXTURES = [
    ('4', ('4', True)),
    ('5', ('5', True)),
    ('1', ('1', False)), 
    ('2', ('2', False)), 
    ('3', ('3', False))
]

class TestFunctions(unittest.TestCase):

    def SetUp(self):
        print('method SetUp')

    def TearDowm(self):
        print('method TearDown')

    @parameterized.expand(FIXTURES)
    def test_add_new_shelf(self, shelf_number, expected_result):
        result = add_new_shelf(shelf_number)
        self.assertEqual(expected_result, result)