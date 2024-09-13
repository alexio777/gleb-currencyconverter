from fastapi import HTTPException
from typing import List

from src.converter.services.enums.exchangerate_response import ResponseErrorType


class BaseExchangeRateException(HTTPException):
    def __init__(self, detail: str = None):
        super().__init__(status_code=400, detail=detail)


class UnsupportedCurrencyCode(HTTPException):
    def __init__(self, to_currency: str, supported_currencies: List[str]):
        detail = (
            f"{ResponseErrorType.UNSUPPORTED_CURRENCY_TYPE.name}: {to_currency}. "
            f"Supported currencies for conversion: {supported_currencies}"
        )
        super().__init__(status_code=400, detail=detail)
