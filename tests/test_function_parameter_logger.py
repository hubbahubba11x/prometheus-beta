import logging
import pytest
from src.function_parameter_logger import log_parameters

# Create a custom logger for testing
class MockLogger:
    def __init__(self):
        self.logged_messages = []
    
    def info(self, message):
        self.logged_messages.append(message)

def test_log_parameters_basic():
    """Test basic parameter logging functionality"""
    mock_logger = MockLogger()
    
    @log_parameters(logger=mock_logger)
    def sample_function(a, b, c=10):
        return a + b + c
    
    # Call the function
    result = sample_function(1, 2)
    
    # Check the result
    assert result == 13
    
    # Check logged messages
    assert len(mock_logger.logged_messages) == 1
    log_message = mock_logger.logged_messages[0]
    
    # Verify log message contains function name and parameters
    assert "sample_function" in log_message
    assert "a: 1" in log_message
    assert "b: 2" in log_message
    assert "c: 10" in log_message

def test_log_parameters_different_types():
    """Test logging with different parameter types"""
    mock_logger = MockLogger()
    
    @log_parameters(logger=mock_logger)
    def complex_function(int_param: int, str_param: str, list_param: list = None):
        return f"{int_param} {str_param} {list_param}"
    
    # Call with various types
    result = complex_function(42, "hello", [1, 2, 3])
    
    # Check the result
    assert result == "42 hello [1, 2, 3]"
    
    # Check logged messages
    assert len(mock_logger.logged_messages) == 1
    log_message = mock_logger.logged_messages[0]
    
    # Verify log message contains function name and parameters
    assert "complex_function" in log_message
    assert "int_param: 42" in log_message
    assert "str_param: 'hello'" in log_message
    assert "list_param: [1, 2, 3]" in log_message

def test_log_parameters_default_logger():
    """Test that a default logger is created if none is provided"""
    # This test checks that no exception is raised when no logger is specified
    @log_parameters()
    def no_logger_function(x, y):
        return x + y
    
    # Should not raise any exceptions
    result = no_logger_function(5, 7)
    assert result == 12

def test_log_parameters_kwargs():
    """Test logging with keyword arguments"""
    mock_logger = MockLogger()
    
    @log_parameters(logger=mock_logger)
    def kwargs_function(**kwargs):
        return sum(kwargs.values())
    
    # Call with keyword arguments
    result = kwargs_function(a=1, b=2, c=3)
    
    # Check the result
    assert result == 6
    
    # Check logged messages
    assert len(mock_logger.logged_messages) == 1
    log_message = mock_logger.logged_messages[0]
    
    # Verify log message contains function name and parameters
    assert "kwargs_function" in log_message
    assert "a: 1" in log_message
    assert "b: 2" in log_message
    assert "c: 3" in log_message