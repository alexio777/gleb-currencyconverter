from enum import Enum


class ResponseErrorType(Enum):
    UNSUPPORTED_CURRENCY_TYPE = 'unsupported-code'
    INVALID_API_KEY = "invalid-key"
    REQUESTS_LIMIT_REACHED = "quota-reached"
    INACTIVE_ACCOUNT = "inactive-account"

    @classmethod
    def values(cls):
        return tuple(item.value for item in cls)
