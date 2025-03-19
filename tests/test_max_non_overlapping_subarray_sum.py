import pytest
from src.max_non_overlapping_subarray_sum import max_non_overlapping_subarray_sum

def test_basic_positive_array():
    """Test with a basic positive integer array."""
    assert max_non_overlapping_subarray_sum([1, 2, 3, 4, 5]) == 9
    
def test_mixed_array():
    """Test with a mixed array of positive and negative integers."""
    assert max_non_overlapping_subarray_sum([-1, -2, 3, 4]) == 4
    assert max_non_overlapping_subarray_sum([1, -2, 3, -4, 5]) == 6
    
def test_empty_array():
    """Test with an empty array."""
    assert max_non_overlapping_subarray_sum([]) == 0
    
def test_single_element_array():
    """Test with a single element array."""
    assert max_non_overlapping_subarray_sum([10]) == 10
    assert max_non_overlapping_subarray_sum([-5]) == 0
    
def test_all_negative_array():
    """Test with an array of all negative numbers."""
    assert max_non_overlapping_subarray_sum([-1, -2, -3]) == 0
    
def test_longer_complex_array():
    """Test with a more complex longer array."""
    assert max_non_overlapping_subarray_sum([2, 3, 4, 5, 6, 1, 2]) == 17
    
def test_invalid_input_type():
    """Test with invalid input type."""
    with pytest.raises(TypeError, match="Input must be a list"):
        max_non_overlapping_subarray_sum("not a list")
    
def test_invalid_element_type():
    """Test with non-integer elements."""
    with pytest.raises(ValueError, match="All elements must be integers"):
        max_non_overlapping_subarray_sum([1, 2, "3", 4])
        
def test_zero_array():
    """Test with an array containing only zeros."""
    assert max_non_overlapping_subarray_sum([0, 0, 0]) == 0