import pytest
from src.palindrome_validator import is_palindrome

def test_classic_palindromes():
    """Test well-known palindrome phrases"""
    assert is_palindrome("A man, a plan, a canal: Panama") == True
    assert is_palindrome("race a car") == False

def test_simple_palindromes():
    """Test simple palindrome scenarios"""
    assert is_palindrome("racecar") == True
    assert is_palindrome("hello") == False

def test_edge_cases():
    """Test edge cases"""
    assert is_palindrome("") == True  # Empty string
    assert is_palindrome(" ") == True  # Only whitespace
    assert is_palindrome("!@#$%^&*()") == True  # Only special characters

def test_case_insensitivity():
    """Test case insensitivity"""
    assert is_palindrome("Able was I ere I saw Elba") == True

def test_mixed_characters():
    """Test palindromes with mixed characters"""
    assert is_palindrome("Do geese see God?") == True
    assert is_palindrome("Was it a car or a cat I saw?") == True

def test_non_palindromes():
    """Test various non-palindrome strings"""
    assert is_palindrome("python") == False
    assert is_palindrome("not a palindrome") == False

def test_numeric_palindromes():
    """Test numeric palindromes"""
    assert is_palindrome("123321") == True
    assert is_palindrome("12345") == False