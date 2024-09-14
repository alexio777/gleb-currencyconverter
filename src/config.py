from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    EXCHANGE_RATES_BASE_URL: str = "https://v6.exchangerate-api.com/v6"
    EXCHANGE_RATES_VERSION: str = "latest"
    API_KEY: str | None = None
    API_EXCHANGE_RATES_KEY: str | None = None
    CACHE_TTL: int = 60  # seconds

    class Config:
        env_file = ".env"
        extra = "ignore"


settings = Settings()
