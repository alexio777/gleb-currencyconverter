from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    EXCHANGE_RATES_BASE_URL: str = "https://v6.exchangerate-api.com/v6"
    EXCHANGE_RATES_VERSION: str = "latest"
    API_KEY: str
    API_EXCHANGE_RATES_KEY: str

    class Config:
        env_file = ".env"


settings = Settings()
