# Contributing

Thank you for your interest in contributing to MyLib! This guide will help you get started.

## Getting Started

### 1. Fork the Repository

```bash
# Click "Fork" on GitHub
# Then clone your fork
git clone https://github.com/yourusername/gh-pages-ex.git
cd gh-pages-ex
```

### 2. Set Up Development Environment

```bash
# Create a virtual environment
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

# Install in development mode with dev dependencies
pip install -e .
pip install -r requirements-dev.txt
```

### 3. Create a Branch

```bash
git checkout -b feature/your-feature-name
```

## Development Workflow

### Making Changes

1. **Implement your feature/fix**
   ```bash
   # Edit files in mylib/
   # Add/update docstrings
   # Write tests
   ```

2. **Run tests locally**
   ```bash
   pytest tests/  # If tests exist
   ```

3. **Build documentation locally**
   ```bash
   cd docs
   make clean
   make html
   open _build/html/index.html
   ```

4. **Commit your changes**
   ```bash
   git add .
   git commit -m "Add feature: description"
   ```

5. **Push to your fork**
   ```bash
   git push origin feature/your-feature-name
   ```

6. **Create a Pull Request**
   - Go to the original repository
   - Click "New Pull Request"
   - Select your branch
   - Add a description of your changes

## Coding Guidelines

### Follow PEP 8

```bash
# Use a linter to check code style
flake8 mylib/
pylint mylib/
```

### Write Tests

Every new feature should have tests:

```python
# In tests/test_core.py
def test_calculator_add():
    calc = Calculator()
    result = calc.add(5, 3)
    assert result == 8

def test_calculator_divide_by_zero():
    calc = Calculator()
    with pytest.raises(ValueError):
        calc.divide(10, 0)
```

### Document Your Code

```python
def my_new_function(param: str) -> str:
    """Brief description of what the function does.
    
    More detailed explanation if needed.
    
    Args:
        param: Description of the parameter.
    
    Returns:
        Description of the return value.
    
    Raises:
        ValueError: When something goes wrong.
    
    Example:
        >>> my_new_function("input")
        'output'
    """
    pass
```

### Docstring Checklist

- [ ] Function has a docstring
- [ ] Docstring starts with a one-line summary
- [ ] Args section documents all parameters
- [ ] Returns section describes the return value
- [ ] Raises section lists exceptions
- [ ] Example shows typical usage
- [ ] Type hints are present

## Adding a New Module

If you're adding a new module to MyLib:

### 1. Create the Module

```bash
# Create mylib/newmodule.py
# Add your functions/classes with docstrings
```

### 2. Update Exports

Edit `mylib/__init__.py`:

```python
from .newmodule import my_function

__all__ = [
    "Calculator",
    "format_text", 
    "add_prefix",
    "my_function",  # Add your export
]
```

### 3. Create Documentation

Create `docs/api/newmodule.rst`:

```rst
New Module
==========

.. automodule:: mylib.newmodule
   :members:
   :undoc-members:
   :show-inheritance:
```

### 4. Update Documentation Index

Edit `docs/api/index.rst`:

```rst
.. toctree::
   :maxdepth: 2

   core
   utils
   newmodule  # Add your module
```

## Adding Documentation

To add guides or documentation:

### Markdown Guides

1. Create a file in `docs/guides/` or `resources/`
2. Write in Markdown format
3. Update the relevant `index.rst` or `index.md` file
4. Push your changes

### Example

```markdown
# My Guide Title

This is my guide content.

## Section 1

Some explanation.

```python
# Code example
code_here()
```
```

## Commit Message Format

Use clear, descriptive commit messages:

```
Add feature: brief description

Longer explanation of what was changed and why.
Can span multiple lines.

Fixes #123
```

### Examples

- ✅ `Add divide method with zero-check`
- ✅ `Fix typo in Calculator docstring`
- ✅ `Update getting started guide with new example`
- ❌ `Fix stuff`
- ❌ `Update`

## Pull Request Guidelines

### Before Submitting

- [ ] Code follows PEP 8 style guide
- [ ] All docstrings are present and complete
- [ ] Tests pass (if applicable)
- [ ] Documentation builds without errors
- [ ] Commit messages are clear and descriptive
- [ ] Branch is up to date with main

### In Your PR Description

Include:

```markdown
## Description

Brief description of what this PR does.

## Changes

- Change 1
- Change 2
- Change 3

## Testing

How did you test these changes?

## Related Issues

Fixes #123
Related to #456
```

## Code Review Process

1. **Automated Checks**: GitHub Actions runs tests and builds documentation
2. **Manual Review**: Maintainers review your code
3. **Feedback**: Address any requested changes
4. **Approval**: When approved, maintainers will merge
5. **Merged**: Your changes are live!

## Reporting Issues

Found a bug? Have a suggestion?

1. **Search existing issues** to avoid duplicates
2. **Create a new issue** with:
   - Clear title
   - Detailed description
   - Steps to reproduce (for bugs)
   - Expected vs. actual behavior
   - Python version and environment info

### Bug Report Template

```markdown
## Description
Brief description of the bug.

## Steps to Reproduce
1. Import mylib
2. Do something
3. Error occurs

## Expected Behavior
What should happen?

## Actual Behavior
What actually happened?

## Environment
- Python version: 3.11
- OS: macOS
- mylib version: 0.1.0
```

## Development Tips

### Using a Virtual Environment

```bash
# Create
python -m venv venv

# Activate
source venv/bin/activate  # macOS/Linux
venv\Scripts\activate      # Windows

# Deactivate
deactivate
```

### Building Documentation

```bash
cd docs

# Clean and rebuild
make clean && make html

# View in browser
open _build/html/index.html
```

### Running Code Analysis

```bash
# Check code style
flake8 mylib/

# Check type hints
mypy mylib/

# Check imports
pylint mylib/
```

## Questions?

- Check the [API Reference](../api/index)
- Read the [Getting Started Guide](../guides/getting_started)
- Review [Best Practices](best_practices.md)
- Open a GitHub issue

## Code of Conduct

Please note that this project is released with a Contributor Code of Conduct. By participating in this project you agree to abide by its terms.

## License

By contributing, you agree that your contributions will be licensed under the same license as the project (typically MIT).

---

Thank you for contributing! 🎉
