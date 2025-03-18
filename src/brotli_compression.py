import brotli
from typing import Union, Optional

def brotli_compress(data: Union[str, bytes], quality: int = 6, mode: Optional[int] = None) -> bytes:
    """
    Compress data using the Brotli compression algorithm.

    Args:
        data (str or bytes): The data to be compressed. Can be a string or bytes.
        quality (int, optional): Compression level (0-11). Defaults to 6.
                                 0 is fastest, 11 is most compressed.
        mode (int, optional): Compression mode. 
                               Defaults to None (uses brotli.MODE_GENERIC).
                               Can be MODE_GENERIC, MODE_TEXT, or MODE_FONT.

    Returns:
        bytes: Compressed data

    Raises:
        TypeError: If input is not str or bytes
        ValueError: If quality is out of valid range
    """
    # Validate input type
    if not isinstance(data, (str, bytes)):
        raise TypeError("Input must be str or bytes")
    
    # Convert string to bytes if necessary
    if isinstance(data, str):
        data = data.encode('utf-8')
    
    # Validate compression quality
    if not 0 <= quality <= 11:
        raise ValueError("Compression quality must be between 0 and 11")
    
    # Use default mode if not specified
    if mode is None:
        mode = brotli.MODE_GENERIC
    
    # Perform Brotli compression
    try:
        return brotli.compress(data, mode=mode, quality=quality)
    except Exception as e:
        raise RuntimeError(f"Compression failed: {str(e)}")

def brotli_decompress(compressed_data: bytes) -> bytes:
    """
    Decompress Brotli compressed data.

    Args:
        compressed_data (bytes): Brotli compressed data

    Returns:
        bytes: Decompressed data

    Raises:
        TypeError: If input is not bytes
        RuntimeError: If decompression fails
    """
    # Validate input type
    if not isinstance(compressed_data, bytes):
        raise TypeError("Input must be bytes")
    
    # Perform Brotli decompression
    try:
        return brotli.decompress(compressed_data)
    except Exception as e:
        raise RuntimeError(f"Decompression failed: {str(e)}")