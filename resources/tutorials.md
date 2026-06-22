# Tutorials

This tutorial shows how to use MyLib to build a simple text-processing application.

## Getting started

Install the package in editable mode:

```bash
pip install -e .
```

Create a new Python file and import the needed classes and functions:

```python
from mylib import Calculator, format_text, add_prefix, reverse_string
```
```

## Example application

Use `Calculator` and the utility helpers to process text and compute values:

```python
from mylib import Calculator, format_text, add_prefix

calc = Calculator()
result = calc.add(5, 3)
text = format_text("hello world", uppercase=True)
text = add_prefix(text, "RESULT")
print(result)
print(text)
```

## Next steps

- Use `format_text` for normalization
- Use `Calculator` for numeric operations
- Use `add_prefix` to label outputs
