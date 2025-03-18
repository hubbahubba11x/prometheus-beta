import os
import pytest
import tempfile

from src.file_exists import check_file_exists

def test_existing_file():
    """Test that the function returns True for an existing file."""
    with tempfile.NamedTemporaryFile(delete=False) as temp_file:
        temp_file_path = temp_file.name
    
    try:
        assert check_file_exists(temp_file_path) == True
    finally:
        # Clean up the temporary file
        os.unlink(temp_file_path)

def test_nonexistent_file():
    """Test that the function returns False for a nonexistent file."""
    assert check_file_exists('nonexistent_file_xyz.txt') == False

def test_directory():
    """Test that the function returns False for a directory."""
    with tempfile.TemporaryDirectory() as temp_dir:
        assert check_file_exists(temp_dir) == False

def test_invalid_input_type():
    """Test that the function raises TypeError for non-string inputs."""
    with pytest.raises(TypeError, match="File path must be a string"):
        check_file_exists(123)
    
    with pytest.raises(TypeError, match="File path must be a string"):
        check_file_exists(None)

def test_empty_string():
    """Test behavior with an empty string path."""
    assert check_file_exists('') == False