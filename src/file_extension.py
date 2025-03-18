def get_file_extension(filename):
    """
    Extract the file extension from a given filename.

    Args:
        filename (str): The name of the file or full file path.

    Returns:
        str: The file extension in lowercase, or an empty string if no extension exists.

    Raises:
        TypeError: If the input is not a string.
    """
    # Check if input is a string
    if not isinstance(filename, str):
        raise TypeError("Filename must be a string")
    
    # Split the filename and get the last part
    parts = filename.split('.')
    
    # If no dot or filename starts with a dot, return empty string
    if len(parts) <= 1 or filename.startswith('.'):
        return ''
    
    # Return the last part (extension) in lowercase
    return parts[-1].lower()