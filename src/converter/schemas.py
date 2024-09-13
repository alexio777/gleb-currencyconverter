from pydantic import BaseModel, Field, condecimal


class ConversionResponse(BaseModel):
    from_currency: str = Field(..., min_length=3, max_length=3)
    to_currency: str = Field(..., min_length=3, max_length=3)
    amount: condecimal(gt=0)
    converted_amount: condecimal(gt=0)

    class Config:
        json_schema_extra = {
            "example": {
                "from_currency": "USD",
                "to_currency": "EUR",
                "amount": 100.0,
                "converted_amount": 85.23
            }
        }
