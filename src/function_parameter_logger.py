import functools
import logging
import inspect

def log_parameters(logger=None):
    """
    A decorator that logs function parameters on invocation.

    Args:
        logger (logging.Logger, optional): Logger to use. 
                If None, creates a default logger.

    Returns:
        callable: Decorated function that logs parameters before execution
    """
    # If no logger is provided, create a default logger
    if logger is None:
        logger = logging.getLogger(__name__)
        # Ensure some basic logging configuration
        if not logger.handlers:
            logging.basicConfig(level=logging.INFO, 
                                format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')

    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            # Get the function signature
            sig = inspect.signature(func)
            
            # Bind the arguments to the function's parameters
            bound_arguments = sig.bind(*args, **kwargs)
            bound_arguments.apply_defaults()
            
            # Create a log message with parameter details
            param_log_str = f"Calling {func.__name__} with parameters:"
            
            # Handle kwargs specifically to expand them
            if 'kwargs' in bound_arguments.arguments:
                kwargs_dict = bound_arguments.arguments['kwargs']
                for param_name, param_value in kwargs_dict.items():
                    param_log_str += f"\n  {param_name}: {repr(param_value)}"
            else:
                # Normal case for regular arguments
                for param_name, param_value in bound_arguments.arguments.items():
                    param_log_str += f"\n  {param_name}: {repr(param_value)}"
            
            # Log the parameters
            logger.info(param_log_str)
            
            # Call the original function
            return func(*args, **kwargs)
        
        return wrapper
    
    return decorator