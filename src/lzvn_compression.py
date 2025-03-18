"""
LZVN Compression Algorithm Implementation

This module provides a basic implementation of the LZVN (LZ Variant N) compression algorithm.
"""

def lzvn_compress(data):
    """
    Compress input data using a basic LZVN-like compression algorithm.
    
    Args:
        data (bytes or bytearray): Input data to compress
    
    Returns:
        bytearray: Compressed data
    
    Raises:
        TypeError: If input is not bytes or bytearray
        ValueError: If input is empty
    """
    # Input validation
    if not isinstance(data, (bytes, bytearray)):
        raise TypeError("Input must be bytes or bytearray")
    
    if not data:
        raise ValueError("Input data cannot be empty")
    
    # Compression variables
    compressed = bytearray()
    window_size = 4096  # Typical sliding window size
    min_match_length = 3  # Minimum length for compression
    
    # Current position in the input data
    pos = 0
    
    while pos < len(data):
        # Look for the longest match in the previous window
        best_length = 0
        best_offset = 0
        
        # Search back in the window for the longest match
        search_start = max(0, pos - window_size)
        for search_pos in range(search_start, pos):
            match_length = 0
            
            # Check how long the match continues
            while (pos + match_length < len(data) and 
                   data[search_pos + match_length] == data[pos + match_length] and 
                   match_length < 255):
                match_length += 1
            
            # Update best match if current match is longer
            if match_length > best_length and match_length >= min_match_length:
                best_length = match_length
                best_offset = pos - search_pos
        
        # Encode the data
        if best_length > 0:
            # Encode a match (use a flag byte to distinguish)
            compressed.append(0xFF)  # Match flag
            compressed.append(best_offset & 0xFF)  # Lower byte of offset
            compressed.append((best_offset >> 8) & 0xFF)  # Upper byte of offset
            compressed.append(best_length)
            pos += best_length
        else:
            # Encode a literal byte
            # Use a literal flag to distinguish
            compressed.append(data[pos])
            pos += 1
    
    return compressed

def lzvn_decompress(compressed_data):
    """
    Decompress data compressed with the LZVN algorithm.
    
    Args:
        compressed_data (bytes or bytearray): Compressed input data
    
    Returns:
        bytearray: Decompressed data
    
    Raises:
        TypeError: If input is not bytes or bytearray
        ValueError: If input is empty or malformed
    """
    # Input validation
    if not isinstance(compressed_data, (bytes, bytearray)):
        raise TypeError("Input must be bytes or bytearray")
    
    if not compressed_data:
        raise ValueError("Compressed data cannot be empty")
    
    # Decompression variables
    decompressed = bytearray()
    pos = 0
    
    while pos < len(compressed_data):
        # Check if we've reached the end of the compressed data
        if pos >= len(compressed_data):
            break
        
        # Check for match flag
        if compressed_data[pos] == 0xFF and pos + 3 < len(compressed_data):
            # This is a match
            # Next 2 bytes are offset, 3rd byte is length
            offset = compressed_data[pos+1] | (compressed_data[pos+2] << 8)
            length = compressed_data[pos+3]
            
            # Copy matched sequence
            if offset == 0 or length == 0:
                raise ValueError("Invalid match: zero offset or length")
            
            start = len(decompressed) - offset
            
            # Bounds checking
            if start < 0:
                raise ValueError("Invalid compressed data: negative offset")
            
            # Reconstruct the matched sequence
            for i in range(length):
                if start + i >= len(decompressed):
                    break
                decompressed.append(decompressed[start + i])
            
            pos += 4  # Move past match encoding
        else:
            # Literal byte
            decompressed.append(compressed_data[pos])
            pos += 1
    
    return decompressed