from datetime import datetime
from typing import Optional

from pydantic import BaseModel


class HealthStatus(BaseModel):
    status: str
    timestamp: datetime
    version: str
    environment: str
    services: dict
    dependencies: dict
    message: Optional[str] = None


class ServiceStatus(BaseModel):
    name: str
    status: str
    message: Optional[str] = None


class DependencyStatus(BaseModel):
    name: str
    version: str
    status: str
    message: Optional[str] = None
