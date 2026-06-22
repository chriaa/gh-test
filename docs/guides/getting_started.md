# Getting Started with MyLib

This guide will help you get started with MyLib quickly.

## Installation

To install MyLib, use pip:

```bash
pip install -e .
```

This will install the package in development mode, allowing you to make changes and see them reflected immediately.

## Basic Usage

### Using the Calculator

The Calculator class provides basic arithmetic operations:

```python
from mylib import Calculator

# Create a calculator instance
calc = Calculator()

# Perform operations
result = calc.add(10, 5)
print(f"10 + 5 = {result}")  # Output: 10 + 5 = 15

result = calc.multiply(4, 3)
print(f"4 × 3 = {result}")  # Output: 4 × 3 = 12

result = calc.divide(20, 4)
print(f"20 ÷ 4 = {result}")  # Output: 20 ÷ 4 = 5.0
```

### Using Utility Functions

The utils module provides helpful text processing functions:

```python
from mylib import format_text, add_prefix, reverse_string

# Format text
text = format_text("hello", uppercase=True)
print(text)  # Output: HELLO

# Add a prefix
prefixed = add_prefix("world", prefix="HELLO")
print(prefixed)  # Output: HELLO_world

# Reverse a string
reversed_text = reverse_string("hello")
print(reversed_text)  # Output: olleh
```

## Next Steps

- Check out the [Tutorial](tutorial.md) for more examples
- Browse the [API Reference](../api/index) for detailed function documentation
- Review the source code to understand implementation details

## Common Issues

### Module Import Error

If you get a `ModuleNotFoundError`, make sure you've installed the package:

```bash
pip install -e .
```

### Documentation Build Error

To rebuild the documentation, navigate to the docs directory and run:

```bash
cd docs
make clean
make html
```

Then open `_build/html/index.html` in your browser.
