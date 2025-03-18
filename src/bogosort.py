import random
from typing import List, TypeVar

T = TypeVar('T')

def is_sorted(arr: List[T]) -> bool:
    """
    Check if the given list is sorted in ascending order.
    
    Args:
        arr (List[T]): The list to check for sorting.
    
    Returns:
        bool: True if the list is sorted, False otherwise.
    """
    return all(arr[i] <= arr[i+1] for i in range(len(arr) - 1))

def bogosort(arr: List[T]) -> List[T]:
    """
    Implement the bogosort (randomsort) algorithm.
    
    Bogosort works by repeatedly shuffling the list randomly until it becomes sorted.
    This is an extremely inefficient sorting algorithm with O(∞) time complexity.
    
    Args:
        arr (List[T]): The list to be sorted.
    
    Returns:
        List[T]: A sorted version of the input list.
    
    Raises:
        ValueError: If the input list is None or empty.
    """
    # Validate input
    if arr is None:
        raise ValueError("Input list cannot be None")
    
    if len(arr) <= 1:
        return arr
    
    # Make a copy to avoid modifying the original list
    working_arr = arr.copy()
    
    # Continue shuffling until the list is sorted
    while not is_sorted(working_arr):
        random.shuffle(working_arr)
    
    return working_arr