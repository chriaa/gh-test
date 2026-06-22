# Project Setup and Build Guide

This document explains the project structure and how to build the documentation.

## Project Structure

```
gh-pages-ex/
├── README.md                 # Project overview
├── setup.py                  # Python package configuration
├── requirements-dev.txt      # Development dependencies
├── .gitignore               # Git ignore rules
├── mylib/                   # Main Python library
│   ├── __init__.py          # Package initialization
│   ├── core.py              # Core functionality (Calculator class)
│   └── utils.py             # Utility functions
└── docs/                    # Sphinx documentation
    ├── conf.py              # Sphinx configuration
    ├── index.rst            # Main documentation index
    ├── Makefile             # Build script
    ├── api/                 # API reference (auto-generated)
    │   ├── index.rst
    │   ├── core.rst
    │   └── utils.rst
    └── guides/              # Custom markdown documentation
        ├── getting_started.md
        └── tutorial.md
```

## Features

### 1. **Python Library (mylib/)**
   - **core.py**: Contains a `Calculator` class with basic arithmetic operations
   - **utils.py**: Contains utility functions for text processing
   - **__init__.py**: Exposes public API

### 2. **Sphinx Documentation**
   - **conf.py**: Sphinx configuration with MyST parser enabled
   - **index.rst**: Main documentation entry point
   - **API Reference**: Auto-generated from Python docstrings using Sphinx autodoc

### 3. **Markdown Support with MyST Parser**
   - **guides/getting_started.md**: Quick start guide
   - **guides/tutorial.md**: Comprehensive tutorial with examples
   - MyST parser integrated in Sphinx configuration allows `.md` files alongside `.rst`

## Installation and Setup

### 1. Install Development Dependencies

```bash
# Navigate to project root
cd /Users/christina/Desktop/gh-pages-ex

# Install development dependencies
pip install -r requirements-dev.txt

# Install the package in development mode
pip install -e .
```

### 2. Build Documentation

```bash
# Navigate to docs directory
cd docs

# Clean previous builds (optional)
make clean

# Build HTML documentation
make html
```

### 3. View Documentation

After building, open the documentation in your browser:

```bash
# macOS
open _build/html/index.html

# Linux
xdg-open _build/html/index.html

# Windows
start _build/html/index.html
```

## Key Technologies

- **Sphinx**: Professional documentation generator
- **MyST Parser**: Allows writing documentation in Markdown instead of just reStructuredText
- **Alabaster**: Clean HTML theme for documentation
- **autodoc**: Automatically generates API documentation from Python docstrings
- **Napoleon**: Support for Google/NumPy style docstrings

## Documentation Features

### Automatic API Documentation
The `.rst` files in `docs/api/` use Sphinx's `autodoc` extension to automatically generate documentation from Python docstrings. When you update the docstrings in `mylib/`, the documentation is automatically updated.

### Markdown Support
Custom guides and tutorials are written in Markdown (`.md` files) and are processed by MyST parser. This allows you to mix Markdown and reStructuredText in your documentation.

### Method Chaining
Both source files use NumPy/Google style docstrings which are automatically converted by the Napoleon extension into nicely formatted documentation.

## Customization

### Adding New Modules
1. Create a new `.py` file in `mylib/`
2. Add it to `mylib/__init__.py` exports
3. Create a `.rst` file in `docs/api/` with:
   ```rst
   Module Name
   ===========
   
   .. automodule:: mylib.module_name
      :members:
      :undoc-members:
      :show-inheritance:
   ```
4. Add it to `docs/api/index.rst` in the toctree

### Adding New Markdown Guides
1. Create a `.md` file in `docs/guides/`
2. Add it to `docs/index.rst` in the toctree:
   ```rst
   .. toctree::
      :maxdepth: 2
      :caption: Contents:
      
      guides/your_new_guide
   ```

### Changing the Theme
Edit `docs/conf.py` and change the `html_theme` variable:
```python
html_theme = 'alabaster'  # Change to 'pyramid', 'agogo', 'nature', etc.
```

## Sphinx Commands

The Makefile in `docs/` provides several build targets:

```bash
make html          # Build HTML documentation
make latexpdf      # Build PDF documentation (requires LaTeX)
make epub          # Build EPUB documentation
make clean         # Remove build directory
make help          # Show all available targets
```

## MyST Parser Configuration

The MyST parser is configured in `conf.py` with:

```python
myst_enable_extensions = [
    "colon_fence",  # Allows fenced code blocks with :::
    "deflist",      # Allows definition lists
]
```

You can extend this with more MyST features as needed.

## Troubleshooting

### Module Import Error During Build
Make sure the library is installed in development mode:
```bash
pip install -e .
```

### MyST Parser Not Found
Install myst-parser:
```bash
pip install myst-parser
```

### CSS/Static Files Not Found
Ensure the `_static` directory exists in `docs/`:
```bash
mkdir -p docs/_static
```

## Next Steps

1. Build the documentation: `cd docs && make html`
2. Review the generated HTML in `docs/_build/html/`
3. Modify `mylib/` code and rebuild to see changes reflected
4. Add more markdown guides as needed
5. Customize the theme and styling in `docs/conf.py`
