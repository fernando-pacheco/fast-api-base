from src.interfaces.base_routes import BaseRoutes


class UserRoutes(BaseRoutes):
    def __init__(self, router, resources):
        super().__init__(router, resources)

    def register_routes(self):
        self.router.post(path="/user", summary="User", tags=["User"])(
            self.resources.user.create_user
        )
