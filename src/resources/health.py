from datetime import datetime, timezone

from src.schemas.health import DependencyStatus, HealthStatus, ServiceStatus


class HealthResource:
    def __init__(self, version, environment):
        self.version = version
        self.environment = environment

    def health_check(self):
        service_status = self._check_services()
        dependency_status = self._check_dependencies()

        return HealthStatus(
            status="healthy",
            timestamp=datetime.now(timezone.utc),
            version=self.version,
            environment=self.environment,
            services=service_status,
            dependencies=dependency_status,
            message="All systems operational",
        )

    def ping(self):
        return HealthStatus(
            status="healthy",
            timestamp=datetime.now(timezone.utc),
            version=self.version,
            environment=self.environment,
            services={},
            dependencies={},
            message="API is responding",
        )

    def _check_services(self):
        return {
            "api": ServiceStatus(
                name="API",
                status="healthy",
                message="API is running",
            ),
        }

    def _check_dependencies(self):
        return {
            "python": DependencyStatus(
                name="Python",
                version="3.13.5",
                status="healthy",
                message="Python environment is healthy",
            ),
        }
