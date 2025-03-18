import pytest
import random
from src.bogosort import bogosort, is_sorted

def test_is_sorted():
    """Test the is_sorted helper function."""
    assert is_sorted([]) == True
    assert is_sorted([1]) == True
    assert is_sorted([1, 2, 3, 4, 5]) == True
    assert is_sorted([1, 3, 2, 4, 5]) == False

def test_bogosort_empty_list():
    """Test bogosort with an empty list."""
    assert bogosort([]) == []

def test_bogosort_single_element():
    """Test bogosort with a single element."""
    assert bogosort([42]) == [42]

def test_bogosort_simple_numbers():
    """Test bogosort with a simple list of numbers."""
    arr = [3, 2, 1]
    result = bogosort(arr)
    assert is_sorted(result)
    assert set(result) == set(arr)

def test_bogosort_with_duplicates():
    """Test bogosort with a list containing duplicate elements."""
    arr = [3, 1, 4, 1, 5, 9, 2, 6]
    result = bogosort(arr)
    assert is_sorted(result)
    assert set(result) == set(arr)

def test_bogosort_string_list():
    """Test bogosort with a list of strings."""
    arr = ['zebra', 'apple', 'banana', 'cat']
    result = bogosort(arr)
    assert is_sorted(result)
    assert set(result) == set(arr)

def test_bogosort_raises_on_none():
    """Test that bogosort raises ValueError when input is None."""
    with pytest.raises(ValueError):
        bogosort(None)

def test_bogosort_randomness(monkeypatch):
    """Verify that bogosort can handle lists with high randomness."""
    # Seed the random number generator for reproducibility
    random.seed(42)
    
    # Create an unsorted list
    arr = [5, 2, 9, 1, 7, 6, 3]
    result = bogosort(arr)
    
    # Assertions
    assert is_sorted(result)
    assert set(result) == set(arr)