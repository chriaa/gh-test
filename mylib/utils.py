"""Utility functions for MyLib."""


def format_text(text, uppercase=False):
    """Format text with optional uppercase conversion.
    
    Args:
        text (str): The input text to format.
        uppercase (bool): If True, convert text to uppercase. Defaults to False.
    
    Returns:
        str: The formatted text.
    
    Example:
        >>> format_text("hello")
        'hello'
        >>> format_text("hello", uppercase=True)
        'HELLO'
    """
    if uppercase:
        return text.upper()
    return text


def add_prefix(text, prefix="PREFIX"):
    """Add a prefix to the given text.
    
    Args:
        text (str): The input text.
        prefix (str): The prefix to add. Defaults to "PREFIX".
    
    Returns:
        str: The text with prefix added.
    
    Example:
        >>> add_prefix("world")
        'PREFIX_world'
        >>> add_prefix("test", prefix="HELLO")
        'HELLO_test'
    """
    return f"{prefix}_{text}"


def reverse_string(text):
    """Reverse a string.
    
    Args:
        text (str): The input string.
    
    Returns:
        str: The reversed string.
    
    Example:
        >>> reverse_string("hello")
        'olleh'
    """
    return text[::-1]
