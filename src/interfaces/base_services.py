from abc import ABC, abstractmethod

from requests import Request


class BaseServices(ABC):
    def __init__(self, requests: Request):
        self.requests = requests

    @abstractmethod
    def get(self):
        pass

    @abstractmethod
    def post(self):
        pass

    @abstractmethod
    def put(self):
        pass

    @abstractmethod
    def delete(self):
        pass
