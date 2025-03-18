import pytest
from src.sponge_case import to_sponge_case

def test_basic_sponge_case():
    """Test basic string conversion to sponge case."""
    assert to_sponge_case("hello") == "HeLlO"
    assert to_sponge_case("python") == "PyThOn"

def test_empty_string():
    """Test empty string handling."""
    assert to_sponge_case("") == ""

def test_single_character():
    """Test single character conversion."""
    assert to_sponge_case("a") == "A"
    assert to_sponge_case("B") == "B"

def test_mixed_case_input():
    """Test conversion of mixed case input."""
    assert to_sponge_case("HeLLo") == "HeLlO"

def test_string_with_spaces():
    """Test conversion of strings with spaces."""
    assert to_sponge_case("hello world") == "HeLlO WoRlD"

def test_special_characters():
    """Test conversion of strings with special characters."""
    assert to_sponge_case("hello, world!") == "HeLlO, WoRlD!"

def test_invalid_input_type():
    """Test raising TypeError for non-string inputs."""
    with pytest.raises(TypeError, match="Input must be a string"):
        to_sponge_case(123)
    
    with pytest.raises(TypeError, match="Input must be a string"):
        to_sponge_case(None)
    
    with pytest.raises(TypeError, match="Input must be a string"):
        to_sponge_case(["hello"])