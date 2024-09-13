from fastapi import APIRouter, Depends, Query
from src.converter.schemas import ConversionResponse
from src.converter.services.conversion import convert_currency
from src.converter.dependencies import verify_api_key

router = APIRouter()


@router.get("/convert", response_model=ConversionResponse)
def convert(
    from_currency: str = Query(..., alias="from", min_length=3, max_length=3, regex="^[A-Z]{3}$"),
    to_currency: str = Query(..., alias="to", min_length=3, max_length=3, regex="^[A-Z]{3}$"),
    amount: float = Query(..., gt=0),
    api_key: str = Depends(verify_api_key)
):
    converted_amount = convert_currency(from_currency, to_currency, amount)

    return {
        "from_currency": from_currency,
        "to_currency": to_currency,
        "amount": amount,
        "converted_amount": converted_amount
    }
