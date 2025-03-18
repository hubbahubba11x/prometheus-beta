import pytest
from src.sentence_case import to_sentence_case

def test_to_sentence_case_basic():
    """Test basic sentence case conversion."""
    assert to_sentence_case("hello world") == "Hello world"
    assert to_sentence_case("HELLO WORLD") == "Hello world"
    assert to_sentence_case("hello WORLD") == "Hello world"

def test_to_sentence_case_single_char():
    """Test sentence case with single character."""
    assert to_sentence_case("a") == "A"
    assert to_sentence_case("Z") == "Z"

def test_to_sentence_case_empty_string():
    """Test sentence case with empty string."""
    assert to_sentence_case("") == ""

def test_to_sentence_case_whitespace():
    """Test sentence case with whitespace strings."""
    assert to_sentence_case(" hello ") == " hello "

def test_to_sentence_case_error_handling():
    """Test error handling for non-string inputs."""
    with pytest.raises(TypeError):
        to_sentence_case(123)
    with pytest.raises(TypeError):
        to_sentence_case(None)
    with pytest.raises(TypeError):
        to_sentence_case(["hello"])