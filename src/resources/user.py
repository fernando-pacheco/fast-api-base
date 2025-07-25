from fastapi import Depends
from sqlalchemy.ext.asyncio import AsyncSession

from src.infra.database.session import get_session
from src.schemas.user import UserCreateSchema
from src.services.user import UserService


class UserResources:
    async def create_user(
        self,
        payload: UserCreateSchema,
        session: AsyncSession = Depends(get_session),
    ):
        service = UserService(session)
        user = await service.create(payload)
        return user
