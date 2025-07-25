from datetime import datetime
from zoneinfo import ZoneInfo

import jwt
from fastapi import HTTPException, status

BR_TZ = ZoneInfo("America/Sao_Paulo")


def get_token_infos(token):
    try:
        payload = jwt.decode(token, options={"verify_signature": False})

        created_at = datetime.fromtimestamp(payload.get("iat"), tz=BR_TZ)
        expires_at = datetime.fromtimestamp(payload.get("exp"), tz=BR_TZ)
        email = payload.get("email")

        if not email:
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail="Campo 'email' ausente no token",
            )

        return {
            "email": email,
            "created_at": created_at.isoformat(),
            "expires_at": expires_at.isoformat(),
        }

    except jwt.DecodeError as err:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Token malformado ou inválido",
        ) from err
