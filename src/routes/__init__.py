from src.routes.health import HealthCheckRoutes
from src.routes.secure import SecureRoutes
from src.routes.user import UserRoutes


class Routes:
    def __init__(self, app, router, resources):
        self.app = app
        self.router = router
        self.resources = resources
        self.register_routes()
        self.include_router()

    def register_routes(self):
        self.health = HealthCheckRoutes(self.router, self.resources)
        self.secure = SecureRoutes(self.router, self.resources)
        self.user = UserRoutes(self.router, self.resources)

    def include_router(self):
        self.app.include_router(self.router)
