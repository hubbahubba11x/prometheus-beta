from typing import List, TypeVar
import heapq

T = TypeVar('T')

def cartesian_tree_sort(arr: List[T]) -> List[T]:
    """
    Perform Cartesian Tree Sort on the input list using a min-heap.
    
    The key idea of Cartesian Tree Sort is to create a tree from the input 
    where in-order traversal gives a sorted sequence. This implementation 
    uses a heap to achieve a similar sorting process.
    
    Args:
        arr: Input list to be sorted
    
    Returns:
        Sorted list
    
    Raises:
        TypeError: If input is not a list
    """
    if not isinstance(arr, list):
        raise TypeError("Input must be a list")
    
    # If list is empty or has only one element, return as is
    if len(arr) <= 1:
        return arr.copy()
    
    # Create a copy of the input list to preserve original
    input_copy = arr.copy()
    
    # Create a heap (min-heap by default)
    heap = []
    
    # Add index and value to create a stable sort
    for i, val in enumerate(input_copy):
        heapq.heappush(heap, (val, i))
    
    # Result list to store sorted elements
    result = []
    
    # Pop elements from heap to get sorted order
    while heap:
        result.append(heapq.heappop(heap)[0])
    
    return result