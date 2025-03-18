import locale
from typing import Union, Optional

def log_currency_formatted_number(
    number: Union[int, float], 
    currency: Optional[str] = 'USD', 
    decimal_places: int = 2
) -> str:
    """
    Formats and logs a number with a specified currency symbol.

    Args:
        number (int or float): The number to be formatted.
        currency (str, optional): Currency symbol or code. Defaults to 'USD'.
        decimal_places (int, optional): Number of decimal places. Defaults to 2.

    Returns:
        str: Formatted currency string.

    Raises:
        ValueError: If number is negative or decimal_places is negative.
        TypeError: If number is not a numeric type.
    """
    # Validate inputs
    if not isinstance(number, (int, float)):
        raise TypeError("Number must be an integer or float")
    
    if number < 0:
        raise ValueError("Number must be non-negative")
    
    if decimal_places < 0:
        raise ValueError("Decimal places must be non-negative")

    # Currency symbol mapping
    currency_symbols = {
        'USD': '$',
        'EUR': '€',
        'GBP': '£',
        'JPY': '¥'
    }

    # Get symbol or use currency code if not found
    symbol = currency_symbols.get(currency, currency)

    # Format the number with comma separators and specified decimal places
    if decimal_places == 0:
        formatted_number = f"{number:,.0f}"
    else:
        formatted_number = f"{number:,.{decimal_places}f}"

    # Return number with currency symbol (with space for unsupported currencies)
    return f"{currency} {formatted_number}" if currency not in currency_symbols else f"{symbol}{formatted_number}"