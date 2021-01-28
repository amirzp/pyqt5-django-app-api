import requests


class ApiRequest:
    def __init__(self):
        self.__token = None
        self.__refresh = None
        self.__header = None

    def get(self, url: str):
        request = self.request_api(act='get', url=url, header=self.__header)
        if request.status_code == 200:
            return True, request.json()
        else:
            return False, request.json()

    def delete(self, url: str):
        request = self.request_api(act='delete', url=url, header=self.__header)
        return request.json()

    def post(self, url: str, data: dict):
        request = self.request_api(act='post', url=url, data=data, header=self.__header)
        if request.status_code == 201:
            return True
        else:
            return request.json()

    def put(self, url: str, data: dict):
        request = self.request_api(act='put', url=url, data=data, header=self.__header)
        if request.status_code == 200:
            return True
        else:
            return request.json()

    def login(self, data: dict, url: str):
        request = self.request_api(act='post', url=url, data=data)
        if request.status_code == 200:
            request = request.json()
            self.__token = request['access']
            self.__refresh = request['refresh']
            self.__header = {'Authorization': f'Bearer {self.__token}'}
            return True
        else:
            return request.json()

    def register(self, data: dict, url: str):
        request = self.request_api(act='post', url=url, data=data)
        if request.status_code == 201:
            return True
        else:
            return request.json()

    def refresh_token(self):
        pass

    @staticmethod
    def request_api(act: str, url: str, data: dict = None, header: dict = None):
        try:
            if act == 'get':
                request = requests.get(headers=header, url=url)
                return request
            elif act == 'post':
                request = requests.post(headers=header, json=data, url=url)
                return request
            elif act == 'put':
                request = requests.put(headers=header, json=data, url=url)
                return request
            elif act == 'delete':
                class Request:
                    def __init__(self):
                        self.status_code = None
                        self.detail = None

                    def json(self):
                        return {'detail': f'{self.detail}'}

                request_class = Request()
                request = requests.delete(headers=header, url=url)
                if request.status_code == 204:
                    request_class.status_code = 200
                    request_class.detail = 'Item is deleted.'
                else:
                    request_class.status_code = -1
                    request_class.detail = 'Item is not deleted. something wrong!'
                return request_class

        except requests.ConnectionError:
            class Request:
                def __init__(self):
                    self.status_code = -1

                @staticmethod
                def json():
                    return {'detail': 'server is down.'}
            return Request()
