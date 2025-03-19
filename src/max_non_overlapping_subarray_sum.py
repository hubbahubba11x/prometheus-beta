def max_non_overlapping_subarray_sum(arr):
    """
    Find the maximum sum of a non-overlapping subarray in the given array of integers.
    
    A non-overlapping subarray is a contiguous part of the array that does not share 
    any elements with other selected subarrays.
    
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
    
    # If array has only one element, return it
    if len(arr) == 1:
        return arr[0]
    
    # Dynamic programming approach
    # dp[i] represents the maximum sum of non-overlapping subarrays up to index i
    dp = [0] * len(arr)
    dp[0] = max(0, arr[0])
    
    # If second element exists, take max of first two
    if len(arr) > 1:
        dp[1] = max(dp[0], arr[1], arr[0] + arr[1])
    
    # Iterate through the array starting from third element
    for i in range(2, len(arr)):
        # Two choices:
        # 1. Skip current element (take previous max)
        # 2. Take current element + max sum up to two indices before
        dp[i] = max(dp[i-1], dp[i-2] + arr[i], arr[i])
    
    # Return the maximum sum
    return dp[-1]