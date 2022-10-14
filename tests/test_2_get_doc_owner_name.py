import unittest
from parameterized import parameterized
from app import get_doc_owner_name

FIXTURES = [ 
     ('2207 876234', 'Василий Гупкин'), 
    ('11-2', 'Геннадий Покемонов'), 
    ('10006', 'Аристарх Павлов'),
    ('101', None),
    ('333', None),
    ('9 9-1', None)
]

class TestFunctions(unittest.TestCase):

    def SetUp(self):
        print('method SetUp')

    def TearDown(self):
        print('method TearDown')

    @parameterized.expand(FIXTURES)
    def test_get_doc_owner_name(self, user_doc_number, expected_result):
        result = get_doc_owner_name(user_doc_number)
        self.assertEqual(expected_result, result)