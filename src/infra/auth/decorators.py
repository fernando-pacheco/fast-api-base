from functools import wraps

from fastapi import HTTPException, Request, status
from fastapi.security import HTTPBearer

from src.utils.token import get_token_infos

security = HTTPBearer(auto_error=False)


def auth_required(func):
    @wraps(func)
    async def wrapper(*args, **kwargs):
        request: Request = next(
            (arg for arg in args if isinstance(arg, Request)), kwargs.get("request")
        )

        if not request:
            raise HTTPException(status_code=500, detail="Request não encontrado")

        credentials = await security(request)

        if not credentials:
            raise HTTPException(
                status_code=status.HTTP_403_FORBIDDEN,
                detail="Token de autenticação não fornecido",
            )

        token = credentials.credentials
        payload = get_token_infos(token)

        request.state.jwt_payload = payload

        return await func(*args, **kwargs)

    return wrapper
