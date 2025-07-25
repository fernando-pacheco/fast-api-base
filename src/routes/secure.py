from src.docs.secure.description import secure_description
from src.interfaces.base_routes import BaseRoutes
from src.schemas.secure import TokenResponse


class SecureRoutes(BaseRoutes):
    def __init__(self, router, resources):
        super().__init__(router, resources)

    def register_routes(self):
        self.router.get(
            path="/secure",
            summary="Secure",
            description=secure_description,
            tags=["Security"],
            response_model=TokenResponse,
        )(self.resources.secure.private_data)
