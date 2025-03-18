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

    # Set up locale for currency formatting
    try:
        # Map currency to locale settings
        currency_locales = {
            'USD': 'en_US.UTF-8',
            'EUR': 'de_DE.UTF-8',
            'GBP': 'en_GB.UTF-8',
            'JPY': 'ja_JP.UTF-8'
        }
        
        # Use specified locale or default to USD
        locale_setting = currency_locales.get(currency, 'en_US.UTF-8')
        locale.setlocale(locale.LC_ALL, locale_setting)
        
        # Format the number with specified decimal places
        formatted_number = locale.currency(number, grouping=True, symbol=True, 
                                           decimal_digits=decimal_places)
        
        return formatted_number
    except locale.Error:
        # Fallback to basic formatting if locale is not supported
        return f"{currency} {number:.{decimal_places}f}"