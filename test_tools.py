from tools.exchange_rate import get_exchange_rate
from tools.currency_converter import currency_converter
from tools.currency_info import currency_information

print(get_exchange_rate.invoke({"from_currency": "USD", "to_currency": "INR"}))

print(
    currency_converter.invoke(
        {"amount": 1000, "from_currency": "USD", "to_currency": "INR"}
    )
)

print(currency_information.invoke({"currency_code": "AED"}))
