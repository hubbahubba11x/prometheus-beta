import pytest
from src.file_extension import get_file_extension

def test_normal_file_extension():
    """Test getting extension for a typical filename"""
    assert get_file_extension('document.txt') == 'txt'
    assert get_file_extension('image.JPG') == 'jpg'

def test_multiple_dots():
    """Test filename with multiple dots"""
    assert get_file_extension('archive.tar.gz') == 'gz'
    assert get_file_extension('my.awesome.file.txt') == 'txt'

def test_no_extension():
    """Test files without extensions"""
    assert get_file_extension('README') == ''
    assert get_file_extension('filename') == ''

def test_hidden_files():
    """Test hidden files or files starting with a dot"""
    assert get_file_extension('.gitignore') == ''
    assert get_file_extension('.bashrc') == ''

def test_full_path():
    """Test getting extension from full file paths"""
    assert get_file_extension('/home/user/document.pdf') == 'pdf'
    assert get_file_extension('C:\\Users\\name\\file.docx') == 'docx'

def test_error_handling():
    """Test error handling for invalid inputs"""
    with pytest.raises(TypeError):
        get_file_extension(None)
    with pytest.raises(TypeError):
        get_file_extension(123)
    with pytest.raises(TypeError):
        get_file_extension(['file.txt'])