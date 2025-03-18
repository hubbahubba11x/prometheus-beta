import pytest
from src.cartesian_tree_sort import cartesian_tree_sort

def test_cartesian_tree_sort_basic():
    """Test basic sorting functionality"""
    arr = [3, 1, 4, 1, 5, 9, 2, 6]
    sorted_arr = cartesian_tree_sort(arr)
    assert sorted_arr == sorted(arr)

def test_cartesian_tree_sort_empty_list():
    """Test sorting an empty list"""
    arr = []
    sorted_arr = cartesian_tree_sort(arr)
    assert sorted_arr == []

def test_cartesian_tree_sort_single_element():
    """Test sorting a list with a single element"""
    arr = [42]
    sorted_arr = cartesian_tree_sort(arr)
    assert sorted_arr == [42]

def test_cartesian_tree_sort_already_sorted():
    """Test sorting an already sorted list"""
    arr = [1, 2, 3, 4, 5]
    sorted_arr = cartesian_tree_sort(arr)
    assert sorted_arr == arr

def test_cartesian_tree_sort_reverse_sorted():
    """Test sorting a reverse sorted list"""
    arr = [5, 4, 3, 2, 1]
    sorted_arr = cartesian_tree_sort(arr)
    assert sorted_arr == sorted(arr)

def test_cartesian_tree_sort_with_duplicates():
    """Test sorting a list with duplicate elements"""
    arr = [3, 3, 1, 4, 1, 5, 9, 2, 6, 5]
    sorted_arr = cartesian_tree_sort(arr)
    assert sorted_arr == sorted(arr)

def test_cartesian_tree_sort_type_error():
    """Test raising TypeError for non-list input"""
    with pytest.raises(TypeError, match="Input must be a list"):
        cartesian_tree_sort("not a list")

def test_cartesian_tree_sort_negative_numbers():
    """Test sorting a list with negative numbers"""
    arr = [-3, 0, -1, 4, -2, 6]
    sorted_arr = cartesian_tree_sort(arr)
    assert sorted_arr == sorted(arr)

def test_cartesian_tree_sort_mixed_numbers():
    """Test sorting a mix of positive and negative numbers"""
    arr = [10, -5, 0, 15, -10, 20]
    sorted_arr = cartesian_tree_sort(arr)
    assert sorted_arr == sorted(arr)