import os
import pytest
from cryptography.fernet import Fernet
from src.file_encryption import generate_key, encrypt_file

class TestFileEncryption:
    @pytest.fixture
    def sample_text_file(self, tmp_path):
        """Create a temporary input file for testing."""
        input_file = tmp_path / "sample.txt"
        input_file.write_text("This is a test file for encryption.")
        return str(input_file)

    def test_generate_key(self):
        """Test key generation produces a valid Fernet key."""
        key = generate_key()
        assert isinstance(key, bytes)
        assert len(key) > 0
        # Verify the key can be used to create a Fernet instance
        try:
            Fernet(key)
        except Exception as e:
            pytest.fail(f"Generated key is invalid: {e}")

    def test_encrypt_file_success(self, sample_text_file, tmp_path):
        """Test successful file encryption."""
        key = generate_key()
        output_file = str(tmp_path / "encrypted.bin")
        
        # Encrypt the file
        encrypt_file(sample_text_file, output_file, key)
        
        # Verify encrypted file was created
        assert os.path.exists(output_file)
        assert os.path.getsize(output_file) > 0
        
        # Verify file contents are different
        with open(sample_text_file, 'rb') as f:
            original_data = f.read()
        with open(output_file, 'rb') as f:
            encrypted_data = f.read()
        
        assert original_data != encrypted_data

    def test_encryption_input_file_not_found(self, tmp_path):
        """Test encryption fails when input file doesn't exist."""
        key = generate_key()
        non_existent_file = str(tmp_path / "non_existent.txt")
        output_file = str(tmp_path / "encrypted.bin")
        
        with pytest.raises(FileNotFoundError):
            encrypt_file(non_existent_file, output_file, key)

    def test_encryption_empty_key(self, sample_text_file, tmp_path):
        """Test encryption fails with empty key."""
        output_file = str(tmp_path / "encrypted.bin")
        
        with pytest.raises(ValueError, match="Encryption key cannot be empty"):
            encrypt_file(sample_text_file, output_file, b'')