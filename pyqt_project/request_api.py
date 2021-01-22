import requests


class ApiRequest:
    def __init__(self):
        self.__token = None
        self.__refresh = None
        self.__id = None

    def login(self, data: dict, url: str):
        request = self.request_api(act='get', url=url, data=data)
        if request.status_code == 200:
            request = request.json()
            self.__token = request['access']
            self.__refresh = request['refresh']
            return True
        else:
            return request.json()

    def refresh(self):
        pass

    @staticmethod
    def request_api(act: str, url: str, data: dict = None):
        try:
            if act == 'get':
                request = requests.post(json=data, url=url)
                return request
            elif act == 'post':
                pass
            elif act == 'put':
                pass
            elif act == 'delete':
                pass
        except requests.ConnectionError:
            class Request:
                def __init__(self):
                    self.status_code = 0

                @staticmethod
                def json():
                    return {'detail': 'server is down.'}
            return Request()


if __name__ == '__main__':
    api = ApiRequest()
    d = {
        "username": "amir",
        "password": "123"
    }
    api.login(d, 'http://127.0.0.1:8000/contact/v1/token/')
