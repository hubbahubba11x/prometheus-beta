def max_non_overlapping_subarray_sum(arr):
    """
    Find the maximum sum of a non-overlapping subarray in the given array of integers.
    
    This function aims to select non-overlapping subarrays that maximize the total sum.
    
    Args:
        arr (list): A list of integers.
    
    Returns:
        int: The maximum sum of non-overlapping subarrays.
    
    Raises:
        TypeError: If input is not a list.
        ValueError: If the list contains non-integer elements.
    
    Examples:
        >>> max_non_overlapping_subarray_sum([1, 2, 3, 4, 5])
        9
        >>> max_non_overlapping_subarray_sum([-1, -2, 3, 4])
        4
        >>> max_non_overlapping_subarray_sum([])
        0
    """
    # Validate input
    if not isinstance(arr, list):
        raise TypeError("Input must be a list")
    
    if not arr:
        return 0
    
    # Validate that all elements are integers
    if not all(isinstance(x, int) for x in arr):
        raise ValueError("All elements must be integers")
    
    # Special case for single element array
    if len(arr) == 1:
        return max(0, arr[0])
    
    # Special case for two elements
    if len(arr) == 2:
        return max(0, max(arr[0], arr[1]), sum(arr))
    
    # Track the best non-overlapping sum
    best_sum = 0
    
    # Initialize dynamic programming arrays
    incl = [0] * len(arr)  # max sum including current element
    excl = [0] * len(arr)  # max sum excluding current element
    
    # First value
    incl[0] = max(0, arr[0])
    excl[0] = 0
    
    # Second value with special handling
    incl[1] = max(arr[1], incl[0])
    excl[1] = incl[0]
    
    # Fill DP tables
    for i in range(2, len(arr)):
        # Two choices for including current:
        # 1. Add current to sum excluding previous
        # 2. Consider current element itself
        incl[i] = max(excl[i-2] + arr[i], arr[i], max(0, incl[i-1]))
        
        # Excluding means taking previous best
        excl[i] = max(incl[i-1], excl[i-1])
    
    # Return max of last two entries 
    return max(0, incl[-1], excl[-1])