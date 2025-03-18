import os
import logging
import pytest
import tempfile
from unittest.mock import MagicMock, patch
from src.keystroke_logger import KeystrokeLogger

class MockKeyCode:
    def __init__(self, char):
        self.char = char

class MockKey:
    """Mock special key for testing"""
    def __str__(self):
        return 'MOCK_SPECIAL_KEY'

class TestKeystrokeLogger:
    @pytest.fixture
    def logger(self):
        """Create a temporary log file for each test"""
        with tempfile.NamedTemporaryFile(delete=False, mode='w+', suffix='.log') as temp_log:
            logger = KeystrokeLogger(log_file=temp_log.name)
            yield logger, temp_log.name
            
            # Cleanup: stop logging and remove temp file
            logger.stop_logging()
            os.unlink(temp_log.name)
    
    def test_initialization(self, logger):
        """Test logger initialization"""
        keystroke_logger, log_file = logger
        assert not keystroke_logger.is_active()
        assert keystroke_logger.listener is None
    
    def test_start_logging(self, logger):
        """Test starting logging"""
        keystroke_logger, log_file = logger
        
        # Start logging
        assert keystroke_logger.start_logging() == True
        assert keystroke_logger.is_active() == True
        
        # Try starting again should return False
        assert keystroke_logger.start_logging() == False
    
    def test_stop_logging(self, logger):
        """Test stopping logging"""
        keystroke_logger, log_file = logger
        
        # Start logging first
        keystroke_logger.start_logging()
        
        # Stop logging
        assert keystroke_logger.stop_logging() == True
        assert not keystroke_logger.is_active()
        
        # Try stopping again should return False
        assert keystroke_logger.stop_logging() == False
    
    def test_logging_content(self, logger, caplog):
        """Test that keystrokes are logged correctly"""
        keystroke_logger, log_file = logger
        
        # Capture log messages
        caplog.set_level(logging.INFO)
        
        # Directly call _on_press with different keys
        test_keys = ['a', 'b', 'c']
        for key in test_keys:
            mock_key = MockKeyCode(key)
            keystroke_logger._on_press(mock_key)
        
        # Add a special key
        special_key = MockKey()
        keystroke_logger._on_press(special_key)
        
        # Check log messages
        log_records = [record.message for record in caplog.records]
        
        # Verify that each key was logged
        for key in test_keys:
            assert f"Key pressed: {key}" in log_records
        
        # Check special key logging
        assert f"Special key pressed: {special_key}" in log_records