"""Core functionality module for MyLib."""


class Calculator:
    """A simple calculator class for basic arithmetic operations.
    
    This class provides basic mathematical operations including
    addition, subtraction, multiplication, and division.
    
    Attributes:
        result (float): The result of the last calculation.
    
    Example:
        >>> calc = Calculator()
        >>> calc.add(5, 3)
        8
        >>> calc.multiply(4, 2)
        8
    """
    
    def __init__(self):
        """Initialize the calculator with result set to 0."""
        self.result = 0
    
    def add(self, a, b):
        """Add two numbers.
        
        Args:
            a (float): First number.
            b (float): Second number.
        
        Returns:
            float: The sum of a and b.
        """
        self.result = a + b
        return self.result
    
    def subtract(self, a, b):
        """Subtract two numbers.
        
        Args:
            a (float): First number (minuend).
            b (float): Second number (subtrahend).
        
        Returns:
            float: The difference of a and b.
        """
        self.result = a - b
        return self.result
    
    def multiply(self, a, b):
        """Multiply two numbers.
        
        Args:
            a (float): First number.
            b (float): Second number.
        
        Returns:
            float: The product of a and b.
        """
        self.result = a * b
        return self.result
    
    def divide(self, a, b):
        """Divide two numbers.
        
        Args:
            a (float): Numerator.
            b (float): Denominator.
        
        Returns:
            float: The quotient of a and b.
        
        Raises:
            ValueError: If b is zero.
        """
        if b == 0:
            raise ValueError("Cannot divide by zero")
        self.result = a / b
        return self.result
