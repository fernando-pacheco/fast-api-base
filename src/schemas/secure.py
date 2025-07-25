from pydantic import BaseModel, EmailStr


class UserTokenInfo(BaseModel):
    email: EmailStr
    created_at: str
    expires_at: str


class TokenResponse(BaseModel):
    message: str
    user_token_info: UserTokenInfo
