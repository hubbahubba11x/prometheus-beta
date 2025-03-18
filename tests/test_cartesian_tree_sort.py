import pytest
from src.cartesian_tree_sort import cartesian_tree_sort, build_cartesian_tree, CartesianTreeNode

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

def test_build_cartesian_tree_type_error():
    """Test raising TypeError for non-list input in build_cartesian_tree"""
    with pytest.raises(TypeError, match="Input must be a list"):
        build_cartesian_tree("not a list")

def test_build_cartesian_tree_node_structure():
    """Test the structure of the Cartesian Tree"""
    arr = [3, 1, 4, 1, 5]
    root = build_cartesian_tree(arr)
    
    # Validate node structure
    assert isinstance(root, CartesianTreeNode)
    assert root.value == 1  # Smallest element becomes root
    
    # Additional optional checks for node values based on tree properties
    def validate_heap_property(node):
        """Validate min-heap property"""
        if not node:
            return
        
        if node.left:
            assert node.value <= node.left.value
        
        if node.right:
            assert node.value <= node.right.value
        
        validate_heap_property(node.left)
        validate_heap_property(node.right)
    
    validate_heap_property(root)