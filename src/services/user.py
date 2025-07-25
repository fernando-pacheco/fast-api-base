from src.models.user import UserModel


class UserService:
    def __init__(self, session):
        self.session = session

    async def create(self, payload):
        user = UserModel(**payload.model_dump())
        self.session.add(user)
        await self.session.commit()
        await self.session.refresh(user)
        return user
