from langchain_core.tools import tool

CURRENCY_INFO = {
    "INR": {"country": "India", "currency": "Indian Rupee", "symbol": "₹"},
    "AED": {
        "country": "United Arab Emirates",
        "currency": "UAE Dirham",
        "symbol": "د.إ",
    },
    "USD": {"country": "United States", "currency": "US Dollar", "symbol": "$"},
    "EUR": {"country": "European Union", "currency": "Euro", "symbol": "€"},
    "GBP": {"country": "United Kingdom", "currency": "Pound Sterling", "symbol": "£"},
}


@tool
def currency_information(currency_code: str) -> dict:
    """
    Returns information about a currency.
    """

    currency_code = currency_code.upper().strip()

    if currency_code not in CURRENCY_INFO:

        return {"error": "Unsupported currency."}

    return CURRENCY_INFO[currency_code]
