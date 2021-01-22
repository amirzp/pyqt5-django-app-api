import requests


class ApiRequest:
    def __init__(self):
        self.__token = None
        self.__refresh = None
        self.__id = None

    def login(self, user: str, password: str):
        pass
