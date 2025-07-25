from src.docs.health.description import health_check_description, ping_description
from src.interfaces.base_routes import BaseRoutes
from src.schemas.health import HealthStatus


class HealthCheckRoutes(BaseRoutes):
    def __init__(self, router, resources):
        super().__init__(router, resources)

    def register_routes(self):
        self.router.get(
            path="/health",
            summary="Health Check",
            description=health_check_description,
            tags=["Health"],
            response_model=HealthStatus,
        )(self.resources.health.health_check)

        self.router.get(
            path="/health/ping",
            summary="Ping",
            description=ping_description,
            tags=["Health"],
            response_model=HealthStatus,
        )(self.resources.health.ping)
