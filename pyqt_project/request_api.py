import requests


class ApiRequest:
    def __init__(self):
        self.__token = None
        self.__refresh = None
        self.__header = None

    def get(self, url: str):
        request = self.request_api(act='get', url=url)
        if request.status_code == 200:
            return True, request.json()
        # elif request.status_code == 401:
        #     self.refresh_token()
        #     return self.get(url=url)
        else:
            return False, request.json()

    def delete(self, url: str):
        request = self.request_api(act='delete', url=url)
        return request.json()

    def post(self, url: str, data: dict):
        request = self.request_api(act='post', url=url, data=data)
        if request.status_code == 201:
            return True
        else:
            return request.json()

    def put(self, url: str, data: dict):
        request = self.request_api(act='put', url=url, data=data)
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
        url = 'http://localhost:8000/contact/v1/token/refresh/'
        data = {
            "refresh": f"{self.__refresh}"
        }
        request = self.request_api(act='post', url=url, data=data)
        if request.status_code == 200:
            request_json = request.json()
            self.__token = request_json['access']
            self.__header = {'Authorization': f'Bearer {self.__token}'}
            print('Access token is refreshed.')  # TODO delete this line code

    def request_api(self, act: str, url: str, data: dict = None):
        try:
            if act == 'get':
                request = requests.get(headers=self.__header, url=url)
            elif act == 'post':
                request = requests.post(headers=self.__header, json=data, url=url)
            elif act == 'put':
                request = requests.put(headers=self.__header, json=data, url=url)
            elif act == 'delete':
                class Request:
                    def __init__(self):
                        self.status_code = None
                        self.detail = None

                    def json(self):
                        return {'detail': f'{self.detail}'}

                request_class = Request()
                request = requests.delete(headers=self.__header, url=url)

                if request.status_code == 204:
                    request_class.status_code = 200
                    request_class.detail = 'Item is deleted.'
                elif request.status_code == 401:
                    flag = self.request_test(request)
                    if flag is True:
                        self.refresh_token()
                        return self.request_api(act=act, url=url, data=data)
                    else:
                        request_class.status_code = -1
                        request_class.detail = 'Item is not deleted. something wrong!'
                else:
                    request_class.status_code = -1
                    request_class.detail = 'Item is not deleted. something wrong!'

                return request_class

            flag = self.request_test(request)
            if flag is True:
                self.refresh_token()
                return self.request_api(act=act, url=url, data=data)
            else:
                return request

        except requests.ConnectionError:
            class Request:
                def __init__(self):
                    self.status_code = -1

                @staticmethod
                def json():
                    return {'detail': 'server is down.'}
            return Request()

    @staticmethod
    def request_test(data):
        request = data.json()
        flag = False
        for i in request:
            if i == 'detail':
                flag = True
                break
        if flag is True:
            txt = request['detail'] == "Given token not valid for any token type"
            if data.status_code == 401 and txt:
                return True
            else:
                return False
