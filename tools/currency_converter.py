import requests

from config import EXCHANGE_RATE_API
from utils.logger import logger
from utils.cache import exchange_rate_cache

from langchain_core.tools import tool

BASE_URL = f"https://v6.exchangerate-api.com/v6/{EXCHANGE_RATE_API}"


@tool
def currency_converter(amount: float, from_currency: str, to_currency: str) -> dict:
    """
    Converts an amount from one currency to another
    using the latest exchange rate.
    """

    from_currency = from_currency.upper().strip()
    to_currency = to_currency.upper().strip()

    cache_key = f"{from_currency}_{to_currency}"

    try:

        if cache_key in exchange_rate_cache:

            rate = exchange_rate_cache[cache_key]

            logger.info(f"Cache Hit : {cache_key}")

        else:

            url = f"{BASE_URL}/pair/" f"{from_currency}/{to_currency}"

            response = requests.get(url, timeout=10)

            response.raise_for_status()

            data = response.json()

            if data["result"] != "success":
                raise ValueError(data.get("error-type"))

            rate = data["conversion_rate"]

            exchange_rate_cache[cache_key] = rate

            logger.info(f"Fetched exchange rate : {cache_key}")

        converted_amount = round(amount * rate, 2)

        return {
            "success": True,
            "amount": amount,
            "from_currency": from_currency,
            "to_currency": to_currency,
            "conversion_rate": rate,
            "converted_amount": converted_amount,
        }

    except Exception as e:

        logger.exception(e)

        return {
            "success": False,
            "message": "Unable to fetch exchange rate.",
            "details": str(e),
        }
