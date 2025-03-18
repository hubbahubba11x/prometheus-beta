def to_sponge_case(input_string):
    """
    Convert a string to alternating sponge case (MoCkInG case).
    
    Args:
        input_string (str): The input string to convert.
    
    Returns:
        str: The input string converted to alternating sponge case.
    
    Raises:
        TypeError: If input is not a string.
    
    Examples:
        >>> to_sponge_case("hello")
        'HeLlO'
        >>> to_sponge_case("PYTHON")
        'PyThOn'
        >>> to_sponge_case("")
        ''
    """
    # Check input type
    if not isinstance(input_string, str):
        raise TypeError("Input must be a string")
    
    # If empty string, return empty string
    if not input_string:
        return ""
    
    # Convert to sponge case
    return ''.join(
        char.upper() if i % 2 == 0 else char.lower() 
        for i, char in enumerate(input_string)
    )