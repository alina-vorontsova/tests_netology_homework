import unittest
from yandex_app import Yandex


ya = Yandex()

class TestFunctions(unittest.TestCase):

    def SetUp(self):
        print('method SetUp')
    
    def TearDown(self):
        ya.delete_folder()

    def test_create_new_folder_v1(self):
        '''Тест на положительный ответ.'''
        result = ya.create_new_folder()
        self.assertEqual(201, result)

    def test_create_new_folder_v2(self):
        '''Тест на отрицательный ответ с ошибкой.'''
        result = ya.create_new_folder()
        self.assertEqual(409, result)
