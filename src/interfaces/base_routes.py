from abc import ABC, abstractmethod

from fastapi import APIRouter


class BaseRoutes(ABC):
    def __init__(self, router: APIRouter, resources: object):
        self.router = router
        self.resources = resources
        self.register_routes()

    @abstractmethod
    def register_routes(self):
        """
        Método abstrato para registrar as rotas no router.
        Cada subclasse deve implementar este método.
        """
        pass
