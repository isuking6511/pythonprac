from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    APP_NAME: str = "mlapi"
    ENV: str = "dev"
    # dev는 SQLite, prod는 Postgres
    DATABASE_URL: str = "sqlite:///./app.db"
    JWT_SECRET: str = "change-me"
    JWT_ALG: str = "HS256"
    CORS_ORIGINS: str = "*"
    METRICS_ENABLED: bool = True

    class Config:
        env_file = ".env"

settings = Settings()