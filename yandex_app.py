import requests


with open("ya_token.txt") as f:
    ya_token = f.read()


class Yandex:

    def __init__(self):
        '''Получение параметров авторизации для запроса.'''
        self.token = ya_token
        self.headers = {'Content-Type': 'application/json', 'Authorization': f'OAuth {ya_token}'}
        self.url = 'https://cloud-api.yandex.net/v1/disk/resources'

    def create_new_folder(self, folder_name='Задание'):
        '''Создание новой папки на Я.Диске.'''
        params = {'path': folder_name}
        response = requests.put(self.url, headers=self.headers, params=params)
        return response.status_code

        
    def delete_folder(self, folder_name='Задание'):
        '''Удаление папки на Я.Диске.'''
        params = {'path': folder_name, 'permanently': False}
        response = requests.delete(self.url, headers=self.headers, params=params)
        return response.status_code


if __name__ == '__main__':
    
    ya = Yandex()
    ya.create_new_folder()
    ya.delete_folder()