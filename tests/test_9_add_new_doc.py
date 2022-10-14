import unittest
from parameterized import parameterized
from app import add_new_doc

FIXTURES = [ 
    ('12', 'visa', 'Иван Иваныч', '2', '2'),
    ('666', 'pass', 'Второй Иван', '5', '5')
]

class TestFunctions(unittest.TestCase):

    def SetUp(self):
        print('method SetUp')

    def TearDown(self):
        print('method TearDown')

    @parameterized.expand(FIXTURES)
    def test_add_new_doc(self, new_doc_number, new_doc_type, new_doc_owner_name, new_doc_shelf_number, expected_result):
        result = add_new_doc(new_doc_number, new_doc_type, new_doc_owner_name, new_doc_shelf_number)
        self.assertEqual(expected_result, result)