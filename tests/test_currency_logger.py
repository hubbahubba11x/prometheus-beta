import pytest
import locale
from src.currency_logger import log_currency_formatted_number

def test_default_usd_formatting():
    """Test default USD formatting."""
    result = log_currency_formatted_number(1234.56)
    assert '$' in result
    assert '1,234.56' in result

def test_different_currencies():
    """Test formatting with different currencies."""
    usd = log_currency_formatted_number(1234.56, 'USD')
    eur = log_currency_formatted_number(1234.56, 'EUR')
    gbp = log_currency_formatted_number(1234.56, 'GBP')
    
    assert '$' in usd
    assert '€' in eur or 'EUR' in eur
    assert '£' in gbp or 'GBP' in gbp

def test_decimal_places():
    """Test different decimal place configurations."""
    no_decimals = log_currency_formatted_number(1234, decimal_places=0)
    three_decimals = log_currency_formatted_number(1234.56789, decimal_places=3)
    
    assert '1,234' in no_decimals
    assert '1,234.568' in three_decimals

def test_zero_value():
    """Test formatting zero value."""
    result = log_currency_formatted_number(0)
    assert '$0.00' in result or '0.00' in result

def test_large_number():
    """Test formatting large numbers."""
    result = log_currency_formatted_number(1234567.89)
    assert '1,234,567.89' in result

def test_invalid_inputs():
    """Test error handling for invalid inputs."""
    with pytest.raises(TypeError):
        log_currency_formatted_number('not a number')
    
    with pytest.raises(ValueError):
        log_currency_formatted_number(-100)
    
    with pytest.raises(ValueError):
        log_currency_formatted_number(100, decimal_places=-1)

def test_unsupported_currency():
    """Test handling of unsupported currency."""
    result = log_currency_formatted_number(1234.56, 'XYZ')
    assert 'XYZ 1234.56' in result