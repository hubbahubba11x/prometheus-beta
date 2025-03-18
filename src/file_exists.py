import os

def check_file_exists(file_path):
    """
    Check if a file exists at the specified path.

    Args:
        file_path (str): The path to the file to check.

    Returns:
        bool: True if the file exists and is a file, False otherwise.

    Raises:
        TypeError: If the file_path is not a string.
    """
    # Check if input is a string
    if not isinstance(file_path, str):
        raise TypeError("File path must be a string")
    
    # Use os.path.isfile to check if path exists and is a file
    return os.path.isfile(file_path)