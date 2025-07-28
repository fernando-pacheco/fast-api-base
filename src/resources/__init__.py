from src.resources.health import HealthResource
from src.resources.secure import SecureResource
from src.resources.user import UserResources


class Resources:
    def __init__(self, params):
        self.health = HealthResource(version="1.0.0", environment=params.APP_ENV)
        self.secure = SecureResource()
        self.user = UserResources()
