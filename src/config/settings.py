from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    APP_ENV: str = "dev"
    API_PORT: int = 8000
    API_HOST: str = "0.0.0.0"
    DATABASE_URL: str

    class Config:
        env_file = ".env"
        extra = "ignore"
