import logging
import os
from pynput import keyboard

class KeystrokeLogger:
    """
    A class to log keystrokes entered by the user.
    
    This logger captures and logs keystrokes while providing options 
    for privacy and control.
    """
    
    def __init__(self, log_file='keystrokes.log', log_level=logging.INFO):
        """
        Initialize the KeystrokeLogger.
        
        Args:
            log_file (str, optional): Path to the log file. Defaults to 'keystrokes.log'.
            log_level (int, optional): Logging level. Defaults to logging.INFO.
        """
        # Ensure log directory exists
        os.makedirs(os.path.dirname(log_file) or '.', exist_ok=True)
        
        # Configure logging
        logging.basicConfig(
            filename=log_file, 
            level=log_level, 
            format='%(asctime)s - %(message)s'
        )
        
        self.listener = None
        self.is_logging = False
    
    def _on_press(self, key):
        """
        Callback for key press events.
        
        Args:
            key (keyboard.Key or keyboard.KeyCode): The key that was pressed.
        """
        try:
            # Try to log the character representation of the key
            char = key.char
            logging.info(f"Key pressed: {char}")
        except AttributeError:
            # For special keys (like Enter, Shift, etc.) that don't have a char attribute
            logging.info(f"Special key pressed: {key}")
    
    def start_logging(self):
        """
        Start logging keystrokes.
        
        Returns:
            bool: True if logging started successfully, False if already logging.
        """
        if self.is_logging:
            return False
        
        self.listener = keyboard.Listener(on_press=self._on_press)
        self.listener.start()
        self.is_logging = True
        logging.info("Keystroke logging started")
        return True
    
    def stop_logging(self):
        """
        Stop logging keystrokes.
        
        Returns:
            bool: True if logging stopped successfully, False if not currently logging.
        """
        if not self.is_logging:
            return False
        
        if self.listener:
            self.listener.stop()
            self.listener = None
        
        self.is_logging = False
        logging.info("Keystroke logging stopped")
        return True
    
    def is_active(self):
        """
        Check if keystroke logging is currently active.
        
        Returns:
            bool: True if logging is active, False otherwise.
        """
        return self.is_logging