import pytest
import sys
import os

# Add the src directory to the Python path
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'src')))

from brotli_compression import brotli_compress, brotli_decompress

def test_compress_decompress_string():
    """Test compressing and decompressing a string"""
    original_text = "Hello, world! This is a test of Brotli compression."
    compressed = brotli_compress(original_text)
    decompressed = brotli_decompress(compressed)
    
    assert decompressed.decode('utf-8') == original_text

def test_compress_decompress_bytes():
    """Test compressing and decompressing bytes"""
    original_bytes = b'\x00\x01\x02\x03\x04'
    compressed = brotli_compress(original_bytes)
    decompressed = brotli_decompress(compressed)
    
    assert decompressed == original_bytes

def test_compress_with_different_qualities():
    """Test compression with different quality levels"""
    text = "Test compression at different quality levels"
    
    # Test multiple quality levels
    for quality in [0, 3, 6, 9, 11]:
        compressed = brotli_compress(text, quality=quality)
        decompressed = brotli_decompress(compressed)
        assert decompressed.decode('utf-8') == text

def test_input_type_validation():
    """Test input type validation"""
    # Test invalid input type for compression
    with pytest.raises(TypeError):
        brotli_compress(123)
    with pytest.raises(TypeError):
        brotli_compress(None)
    
    # Test invalid input type for decompression
    with pytest.raises(TypeError):
        brotli_decompress("not bytes")
    with pytest.raises(TypeError):
        brotli_decompress(123)

def test_invalid_compression_quality():
    """Test invalid compression quality"""
    text = "Test compression quality"
    
    # Test quality below range
    with pytest.raises(ValueError):
        brotli_compress(text, quality=-1)
    
    # Test quality above range
    with pytest.raises(ValueError):
        brotli_compress(text, quality=12)

def test_large_input():
    """Test compression and decompression of a large input"""
    large_text = "A" * 100000  # 100,000 character string
    compressed = brotli_compress(large_text)
    decompressed = brotli_decompress(compressed)
    
    assert decompressed.decode('utf-8') == large_text

def test_empty_input():
    """Test compression and decompression of empty input"""
    empty_string = ""
    empty_bytes = b''
    
    # Test empty string
    compressed_str = brotli_compress(empty_string)
    decompressed_str = brotli_decompress(compressed_str)
    assert decompressed_str.decode('utf-8') == empty_string
    
    # Test empty bytes
    compressed_bytes = brotli_compress(empty_bytes)
    decompressed_bytes = brotli_decompress(compressed_bytes)
    assert decompressed_bytes == empty_bytes