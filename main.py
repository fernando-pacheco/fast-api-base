import asyncio

from fastapi import APIRouter, FastAPI
from hypercorn.asyncio import serve
from hypercorn.config import Config

from src.config.settings import Settings
from src.docs.swagger import Swagger
from src.infra.middleware.cors import Cors
from src.infra.middleware.logs.config import Logging
from src.infra.middleware.logs.request import LogRequestMiddleware
from src.resources import Resources
from src.routes import Routes


class Server:
    def __init__(self):
        self._setup_app()
        self._setup_plugins()
        self._setup_middlewares()
        self._setup_server()
        self._setup_modules()

    def _setup_app(self):
        self.app = FastAPI()
        self.router = APIRouter()

    def _setup_plugins(self):
        Logging().configure()
        Cors(self.app).configure()
        Swagger(self.app).configure()

    def _setup_middlewares(self):
        self.app.add_middleware(LogRequestMiddleware)

    def _setup_server(self):
        self.params = Settings()
        self.host = self.params.API_HOST
        self.port = self.params.API_PORT

    def _setup_modules(self):
        self.resources = Resources(self.params)
        self.routes = Routes(self.app, self.router, self.resources)

    def start(self):
        config = Config()
        config.bind = [f"{self.host}:{self.port}"]
        config.loglevel = "debug"
        asyncio.run(serve(self.app, config))


server = Server()
app = server.app

if __name__ == "__main__":
    server.start()
