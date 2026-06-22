# Best Practices

## Code Quality

### Writing Python Code

1. **Follow PEP 8**
   ```python
   # Good
   def calculate_average(numbers):
       return sum(numbers) / len(numbers)
   
   # Avoid
   def calc_avg(n):
     return sum(n)/len(n)
   ```

2. **Use Type Hints**
   ```python
   def add(a: float, b: float) -> float:
       return a + b
   ```

3. **Write Docstrings**
   ```python
   def format_text(text: str, uppercase: bool = False) -> str:
       """Format text with optional uppercase conversion.
       
       Args:
           text: The input text to format.
           uppercase: If True, convert text to uppercase.
       
       Returns:
           The formatted text.
       """
   ```

### Testing

1. **Write Unit Tests**
   ```python
   def test_calculator_add():
       calc = Calculator()
       result = calc.add(5, 3)
       assert result == 8
   ```

2. **Test Edge Cases**
   ```python
   def test_divide_by_zero():
       calc = Calculator()
       with pytest.raises(ValueError):
           calc.divide(10, 0)
   ```

3. **Use Descriptive Test Names**
   - ✅ `test_calculator_divide_by_zero_raises_error`
   - ❌ `test_divide`

## Documentation

### Docstring Style

Use Google-style docstrings (supported by Napoleon extension):

```python
def process_data(data: list, reverse: bool = False) -> list:
    """Process a list of data items.
    
    Args:
        data: List of items to process.
        reverse: If True, reverse the order.
    
    Returns:
        Processed list of items.
    
    Raises:
        ValueError: If data is empty.
    
    Example:
        >>> process_data([1, 2, 3])
        [1, 2, 3]
    """
```

### API Documentation

- Every public function must have a docstring
- Include parameter types and return types
- Provide usage examples
- Document exceptions raised

### Markdown Documentation

- Keep markdown files in `/resources` or `/docs/guides`
- Use clear headings and structure
- Include code examples
- Link to related documentation

## Performance

### Optimization Tips

1. **Avoid Unnecessary Computations**
   ```python
   # Good: compute once
   total = sum(data)
   count = len(data)
   average = total / count
   
   # Avoid: compute multiple times
   average = sum(data) / len(data)
   ```

2. **Use Appropriate Data Structures**
   ```python
   # Good: set for membership testing
   if item in my_set:  # O(1)
   
   # Avoid: list for membership testing
   if item in my_list:  # O(n)
   ```

3. **Profile Before Optimizing**
   ```python
   import cProfile
   cProfile.run('my_function()')
   ```

## Security

### Input Validation

Always validate user input:

```python
def process_text(text: str) -> str:
    """Process text input."""
    if not isinstance(text, str):
        raise TypeError("Input must be a string")
    if len(text) > 1000:
        raise ValueError("Input too long")
    return text.lower()
```

### Error Handling

- Don't expose internal implementation details in errors
- Log security-relevant events
- Handle exceptions gracefully

```python
try:
    result = divide(a, b)
except ValueError as e:
    logger.error(f"Invalid division: {e}")
    return None
```

## Maintainability

### Code Organization

1. **Group Related Functions**
   - Text operations in utils
   - Calculations in core

2. **Keep Functions Small**
   - One responsibility per function
   - Easy to test and understand
   - Typically 10-30 lines

3. **Use Meaningful Names**
   ```python
   # Good
   user_email_addresses = get_user_emails()
   
   # Avoid
   u = get_u()
   ```

### Version Control

- Use clear, descriptive commit messages
- One logical change per commit
- Reference issues when applicable

```
git commit -m "Add divide method to Calculator class

Closes #123. Implements basic division with zero-check."
```

## Dependencies

### Minimize External Dependencies

- Only add dependencies when necessary
- Use well-maintained, popular packages
- Document all dependencies in `requirements-dev.txt`

### Pin Versions

```
sphinx>=4.0.0,<5.0.0
myst-parser>=0.18.0
```

## Documentation Building

### Local Build

```bash
cd docs
make clean
make html
```

### Verify Documentation

- Check for broken links
- Verify code examples work
- Review formatting

## Release Practices

### Version Numbering

Use semantic versioning: `MAJOR.MINOR.PATCH`

- `MAJOR`: Breaking changes
- `MINOR`: New features (backward compatible)
- `PATCH`: Bug fixes

### Changelog

Maintain a CHANGELOG.md:

```
## [0.2.0] - 2026-06-21

### Added
- New reverse_string function

### Fixed
- Division by zero error handling
```

## Common Pitfalls to Avoid

1. ❌ Ignoring edge cases
2. ❌ Poor error messages
3. ❌ Inconsistent naming
4. ❌ Missing documentation
5. ❌ Not testing before committing
6. ❌ Hardcoding values
7. ❌ Not validating input

## Resources

- [PEP 8 Style Guide](https://pep8.org/)
- [Google Python Style Guide](https://google.github.io/styleguide/pyguide.html)
- [Real Python Best Practices](https://realpython.com/)
