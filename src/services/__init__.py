from src.services.user import UserService


class Services:
    def __init__(self, session, params):
        self.user = UserService(session)
