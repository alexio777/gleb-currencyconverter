from typing import Optional

import requests


def send_request(
        url: str,
        request_type: str = "GET",
        payload: Optional[dict] = None,
        query_params: Optional[dict] = None
):

    if not (method := getattr(requests, request_type.lower(), None)):
        raise ValueError(f"Unsupported request type: {request_type}")

    response = method(url, json=payload if request_type == "POST" else None, params=query_params)
    return response.json()
