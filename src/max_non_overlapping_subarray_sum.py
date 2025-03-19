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
    
    # Initialize dynamic programming array
    # dp[i] represents the max non-overlapping sum up to index i
    dp = [0] * len(arr)
    
    # First two elements
    dp[0] = max(0, arr[0])
    dp[1] = max(0, max(arr[0], arr[1]), dp[0] + arr[1])
    
    # Iterate through the array
    for i in range(2, len(arr)):
        # Three choices:
        # 1. Skip current element
        # 2. Take current element + max sum two indices before
        # 3. Take current element and start new subarray
        dp[i] = max(
            dp[i-1],  # skip current
            dp[i-2] + max(0, arr[i]),  # take current with previous non-overlapping
            max(0, arr[i])  # or just current
        )
    
    return dp[-1]