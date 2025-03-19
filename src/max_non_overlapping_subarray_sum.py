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
    
    # Special case for arrays with a few elements
    if len(arr) <= 2:
        return max(0, sum(arr))
    
    # Initialize dynamic programming arrays
    # total[i] tracks best way to include subset of first i elements
    # subset[i] tracks if a subset was used just before this index
    total = [0] * len(arr)
    subset = [False] * len(arr)
    
    # First element
    total[0] = max(0, arr[0])
    subset[0] = total[0] > 0
    
    # Second element 
    total[1] = max(0, total[0], arr[1], total[0] + arr[1])
    subset[1] = total[1] > total[0]
    
    # Fill DP tables
    for i in range(2, len(arr)):
        # Two main strategies:
        # 1. Skip this element and continue previous best
        skip = total[i-1]
        
        # 2. Try creating a new subset ending at current index
        # If previous subset was not used, we can use this new subset
        new_subset_from_prev = (not subset[i-2]) * (total[i-2] + max(0, arr[i]))
        
        # 3. New best isolated subset at this index
        best_subset = max(0, arr[i])
        
        # Combine strategies
        total[i] = max(skip, new_subset_from_prev, best_subset)
        
        # Track if a subset was used
        subset[i] = (total[i] > total[i-1]) and (total[i] > best_subset)
    
    return total[-1]