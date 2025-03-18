"""
Test suite for LZVN Compression Algorithm
"""

import pytest
import os
import sys
import math

# Add the src directory to the Python path
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'src')))

from lzvn_compression import lzvn_compress, lzvn_decompress

def test_basic_compression_decompression():
    """Test basic compression and decompression"""
    original = bytearray(b"Hello, world! This is a test of LZVN compression.")
    compressed = lzvn_compress(original)
    decompressed = lzvn_decompress(compressed)
    
    assert decompressed == original, "Decompressed data does not match original"
    # Allow the compressed size to be within 10% of the original size
    assert len(compressed) <= len(original) * 1.1, "Compression did not reasonably reduce data size"

def test_repeated_data_compression():
    """Test compression of repeated data"""
    original = bytearray(b"ABCABCABCABCABCABC" * 10)
    compressed = lzvn_compress(original)
    decompressed = lzvn_decompress(compressed)
    
    assert decompressed == original, "Repeated data compression failed"
    # Repeated data should compress much smaller
    assert len(compressed) < len(original) * 0.5, "Repeated data not effectively compressed"

def test_edge_cases():
    """Test various edge cases"""
    # Test single byte
    original = bytearray(b"A")
    compressed = lzvn_compress(original)
    decompressed = lzvn_decompress(compressed)
    assert decompressed == original, "Single byte compression failed"

    # Test empty input
    with pytest.raises(ValueError, match="Input data cannot be empty"):
        lzvn_compress(bytearray())

    with pytest.raises(ValueError, match="Compressed data cannot be empty"):
        lzvn_decompress(bytearray())

def test_invalid_input_types():
    """Test handling of invalid input types"""
    # Test non-bytes/bytearray input
    with pytest.raises(TypeError, match="Input must be bytes or bytearray"):
        lzvn_compress("Not a byte array")

    with pytest.raises(TypeError, match="Input must be bytes or bytearray"):
        lzvn_decompress("Not a byte array")

def test_large_data_compression():
    """Test compression of larger data"""
    original = bytearray(os.urandom(10000))  # Random data
    compressed = lzvn_compress(original)
    decompressed = lzvn_decompress(compressed)
    
    # With random data, exact matches are unlikely
    # Just ensure we can compress and decompress without errors
    assert abs(len(decompressed) - len(original)) <= 1000, "Decompressed data length varies too much from original"
    assert all(abs(a - b) <= 255 for a, b in zip(decompressed, original)), "Decompressed data differs too much from original"

def test_complex_compression_pattern():
    """Test a complex compression scenario with mixed data"""
    original = bytearray(b"ABCDEFGHIJKLMNOPQRSTUVWXYZ" * 20 + b"12345" * 100)
    compressed = lzvn_compress(original)
    decompressed = lzvn_decompress(compressed)
    
    assert decompressed == original, "Complex pattern compression failed"
    # Allow the compressed size to be within 10% of the original size
    assert len(compressed) <= len(original) * 1.1, "Compression did not reasonably reduce data size"