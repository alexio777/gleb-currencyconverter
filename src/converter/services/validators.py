from src.converter.services.enums.exchangerate_response import ResponseErrorType
from src.converter.services.exceptions import BaseExchangeRateException


def validate_exchangerate_response(response_data: dict) -> None:
    if "error-type" in response_data:
        error_type = ResponseErrorType(response_data["error-type"])
        raise BaseExchangeRateException(detail=error_type.name)
