from memoization import cached

from src.converter.services.validators import validate_exchangerate_response
from src.converter.services.exceptions import UnsupportedCurrencyCode
from src.converter.config import converter_settings, settings
from src.converter.utils import send_request


@cached(ttl=settings.CACHE_TTL)
def get_exchange_rate(from_currency: str, to_currency: str) -> float:
    url = f"{converter_settings.EXCHANGE_RATES_URL}/{from_currency}"

    print(f"Fetching exchange rate from {url}")

    response_data = send_request(url, request_type="GET")
    validate_exchangerate_response(response_data)

    if to_currency not in response_data.get("conversion_rates", {}):
        raise UnsupportedCurrencyCode(
            to_currency=to_currency,
            supported_currencies=list(response_data.get("conversion_rates", {}).keys()),
        )

    return response_data["conversion_rates"][to_currency]


def convert_currency(from_currency: str, to_currency: str, amount: float) -> float:
    rate = get_exchange_rate(from_currency, to_currency)
    return amount * rate
