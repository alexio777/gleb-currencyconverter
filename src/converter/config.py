from pydantic_settings import BaseSettings
from src.config import settings


class ConverterSettings(BaseSettings):
    EXCHANGE_RATES_URL: str = f"{settings.EXCHANGE_RATES_BASE_URL}/{settings.API_EXCHANGE_RATES_KEY}/{settings.EXCHANGE_RATES_VERSION}"


converter_settings = ConverterSettings()
