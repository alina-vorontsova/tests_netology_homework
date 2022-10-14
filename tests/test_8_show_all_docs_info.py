import unittest
from parameterized import parameterized
from app import show_document_info

FIXTURES = [ 
    ('2207 876234', 'passport "2207 876234" "Василий Гупкин"'),
    ('11-2', 'invoice "11-2" "Геннадий Покемонов"'),
    ('10006', 'insurance "10006" "Аристарх Павлов"')
]

class TestFunctions(unittest.TestCase):

    def SetUp(self):
        print('method SetUp')

    def TearDown(self):
        print('method TearDown')

    @parameterized.expand(FIXTURES)
    def test_show_document_info(self, doc_number, expected_result):
        result = show_document_info(doc_number)
        self.assertEqual(expected_result, result)