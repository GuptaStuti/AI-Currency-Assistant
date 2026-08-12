import requests

from config import EXCHANGE_RATE_API
from utils.logger import logger
from utils.cache import exchange_rate_cache

from langchain_core.tools import tool

BASE_URL = f"https://v6.exchangerate-api.com/v6/{EXCHANGE_RATE_API}"

# BASE_URL = f"https://v6.exchangerate-api.com/v6/{EXCHANGE_RATE_API}"


@tool
def get_exchange_rate(from_currency: str, to_currency: str) -> float:
    """
    Returns the latest exchange rate between two currencies.

    Example:
    from_currency="AED"
    to_currency="INR"
    """

    from_currency = from_currency.upper().strip()
    to_currency = to_currency.upper().strip()

    cache_key = f"{from_currency}_{to_currency}"

    if cache_key in exchange_rate_cache:
        logger.info(f"Cache Hit : {cache_key}")
        return exchange_rate_cache[cache_key]

    url = f"{BASE_URL}/pair/{from_currency}/{to_currency}"

    try:

        response = requests.get(url, timeout=10)

        response.raise_for_status()

        data = response.json()

        if data["result"] != "success":
            raise ValueError(data.get("error-type"))

        rate = data["conversion_rate"]
            
        exchange_rate_cache[cache_key] = rate

        logger.info(f"Fetched exchange rate {from_currency}_{to_currency}")

        return rate

    except Exception as e:

        logger.exception(e)

        raise RuntimeError("Unable to fetch exchange rate.")
