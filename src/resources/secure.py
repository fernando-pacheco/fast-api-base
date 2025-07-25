from fastapi import Request

from src.infra.auth.decorators import auth_required


class SecureResource:
    @auth_required
    async def private_data(self, request: Request):
        jwt_info = request.state.jwt_payload
        return {
            "message": "Token recebido com sucesso",
            "user_token_info": jwt_info,
        }
