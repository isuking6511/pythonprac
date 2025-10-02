from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    APP_NAME: str = "mlapi"
    ENV: str = "dev"
    DATABASE_URL: str = "sqlite:///./app.db"  # 기본 DB는 SQLite
    JWT_SECRET: str = "secret"             # JWT 토큰 서명 키
    JWT_ALG: str = "HS256"                    # 서명 알고리즘
    CORS_ORIGINS: str = "*"                   # 모든 도메인 허용
    METRICS_ENABLED: bool = True              # Prometheus 메트릭 켜기/끄기

    class Config:
        env_file = ".env"

settings = Settings()