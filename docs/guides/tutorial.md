# Tutorial: Building an Application with MyLib

This tutorial demonstrates how to build a simple application using MyLib's components.

## Project: Simple Text Processing Application

In this tutorial, we'll create a text processing application that demonstrates both the Calculator and utility functions from MyLib.

### Step 1: Setting Up Your Project

First, ensure MyLib is installed:

```bash
pip install -e .
```

Create a new Python file called `text_processor.py`:

```python
from mylib import Calculator, format_text, add_prefix, reverse_string
```

### Step 2: Building the Text Processor

Let's create a simple class that uses MyLib functions:

```python
class TextProcessor:
    """A text processor that uses MyLib utilities."""
    
    def __init__(self):
        self.text = ""
        self.calculator = Calculator()
    
    def set_text(self, text):
        """Set the text to process."""
        self.text = text
        return self
    
    def uppercase(self):
        """Convert text to uppercase."""
        self.text = format_text(self.text, uppercase=True)
        return self
    
    def add_prefix(self, prefix="PROCESSED"):
        """Add a prefix to the text."""
        self.text = add_prefix(self.text, prefix=prefix)
        return self
    
    def reverse(self):
        """Reverse the text."""
        self.text = reverse_string(self.text)
        return self
    
    def get_text_length(self):
        """Get the length of the current text."""
        return len(self.text)
    
    def get_word_count(self):
        """Get the number of words in the text."""
        return len(self.text.split())
```

### Step 3: Using the Text Processor

Here's how to use our TextProcessor:

```python
# Create an instance
processor = TextProcessor()

# Chain operations together
result = (processor
    .set_text("hello world")
    .uppercase()
    .add_prefix("GREETING")
    .get_text())

print(result)  # Output: GREETING_HELLO WORLD

# Get statistics
print(f"Text length: {processor.get_text_length()}")
print(f"Word count: {processor.get_word_count()}")
```

### Step 4: Using the Calculator

We can also use the Calculator class for numerical operations:

```python
processor = TextProcessor()
processor.set_text("apple banana cherry")

# Get word count and calculate statistics
word_count = processor.get_word_count()
text_length = processor.get_text_length()

# Use calculator to compute ratios
calc = processor.calculator
avg_word_length = calc.divide(text_length, word_count)
print(f"Average word length: {avg_word_length:.2f}")
```

### Step 5: Advanced Chaining

The TextProcessor supports method chaining for elegant code:

```python
processor = TextProcessor()

# Complex processing pipeline
result = (processor
    .set_text("python programming")
    .uppercase()
    .add_prefix("LANG")
    .get_text())

print(result)  # Output: LANG_PYTHON PROGRAMMING

# Perform calculations
calc = processor.calculator
calc.multiply(processor.get_text_length(), 2)
print(f"Double text length: {calc.result}")
```

## Tips and Best Practices

### Use Method Chaining

When working with TextProcessor, leverage method chaining for cleaner code:

```python
# Good: Clear and readable
result = (processor
    .set_text("hello")
    .uppercase()
    .add_prefix("GREETING")
    .get_text())

# Avoid: Multiple statements
processor.set_text("hello")
processor.uppercase()
processor.add_prefix("GREETING")
```

### Handle Calculator Errors

Always handle division by zero:

```python
try:
    result = calculator.divide(10, 0)
except ValueError as e:
    print(f"Error: {e}")
```

### Use Meaningful Prefixes

Choose descriptive prefixes for better readability:

```python
# Good
text = add_prefix("user_data", prefix="SECURE")

# Less descriptive
text = add_prefix("user_data", prefix="X")
```

## Complete Example

Here's a complete example bringing everything together:

```python
from mylib import Calculator, format_text, add_prefix

class DataProcessor:
    def __init__(self):
        self.data = []
        self.calculator = Calculator()
    
    def add_data(self, item):
        """Add an item to the data list."""
        self.data.append(item)
        return self
    
    def process_item(self, item, uppercase=False, prefix=None):
        """Process an individual item."""
        result = format_text(item, uppercase=uppercase)
        if prefix:
            result = add_prefix(result, prefix=prefix)
        return result
    
    def process_all(self, uppercase=False, prefix=None):
        """Process all items in the data list."""
        return [self.process_item(item, uppercase, prefix) for item in self.data]
    
    def get_stats(self):
        """Get statistics about the data."""
        count = len(self.data)
        total_length = self.calculator.add(0, sum(len(item) for item in self.data))
        avg_length = self.calculator.divide(total_length, count) if count > 0 else 0
        return {
            'count': count,
            'total_length': int(total_length),
            'average_length': avg_length
        }

# Usage
processor = DataProcessor()
processor.add_data("hello").add_data("world").add_data("python")

processed = processor.process_all(uppercase=True, prefix="ITEM")
print(processed)  # Output: ['ITEM_HELLO', 'ITEM_WORLD', 'ITEM_PYTHON']

stats = processor.get_stats()
print(stats)  # Output: {'count': 3, 'total_length': 18, 'average_length': 6.0}
```

## Conclusion

This tutorial demonstrated how to:
- Import and use MyLib components
- Create custom classes that leverage MyLib functionality
- Use method chaining for elegant code
- Combine text processing with calculations

For more details, see the [API Reference](../api/index).
