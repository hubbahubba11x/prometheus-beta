import os
import logging
import pytest
import tempfile
from src.keystroke_logger import KeystrokeLogger
from pynput import keyboard

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
    
    def test_logging_content(self, logger):
        """Test that keystrokes are actually logged"""
        keystroke_logger, log_file = logger
        
        # Start logging
        keystroke_logger.start_logging()
        
        # Simulate a few key presses (using keyboard mock would be more ideal)
        test_keys = ['a', 'b', 'c']
        for key in test_keys:
            keystroke_logger._on_press(keyboard.KeyCode(char=key))
        
        # Stop logging
        keystroke_logger.stop_logging()
        
        # Read log file and check contents
        with open(log_file, 'r') as f:
            log_content = f.read()
        
        # Check that each key is logged
        for key in test_keys:
            assert f"Key pressed: {key}" in log_content
    
    def test_special_key_logging(self, logger):
        """Test logging of special keys"""
        keystroke_logger, log_file = logger
        
        # Start logging
        keystroke_logger.start_logging()
        
        # Simulate a special key press
        special_key = keyboard.Key.enter
        keystroke_logger._on_press(special_key)
        
        # Stop logging
        keystroke_logger.stop_logging()
        
        # Read log file and check contents
        with open(log_file, 'r') as f:
            log_content = f.read()
        
        assert f"Special key pressed: {special_key}" in log_content