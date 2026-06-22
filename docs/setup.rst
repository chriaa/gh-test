Project Setup
=============

This page explains how to set up the MyLib project for local development.

Installation
------------

Step 1: Clone the Repository
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. code-block:: bash

    git clone https://github.com/yourusername/gh-pages-ex.git
    cd gh-pages-ex

Step 2: Install Development Dependencies
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. code-block:: bash

    pip install -r requirements-dev.txt
    pip install -e .

Step 3: Verify Installation
^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. code-block:: bash

    python -c "import mylib; print(mylib.__version__)"

Project Structure
-----------------

The project is organized as follows:

.. code-block:: text

    gh-pages-ex/
    ├── README.md                          # Project overview
    ├── setup.py                           # Package configuration
    ├── requirements-dev.txt               # Development dependencies
    ├── .gitignore                         # Git ignore rules
    ├── mylib/                             # Main Python library
    │   ├── __init__.py                    # Package initialization
    │   ├── core.py                        # Calculator class
    │   └── utils.py                       # Utility functions
    ├── docs/                              # Sphinx documentation
    │   ├── conf.py                        # Sphinx configuration
    │   ├── index.rst                      # Main documentation index
    │   ├── Makefile                       # Build script
    │   ├── api/                           # API reference
    │   │   ├── index.rst
    │   │   ├── core.rst
    │   │   └── utils.rst
    │   └── guides/                        # Custom markdown guides
    │       ├── getting_started.md
    │       └── tutorial.md
    ├── resources/                         # Additional resources
    │   ├── index.md
    │   ├── architecture.md
    │   ├── best_practices.md
    │   └── contributing.md
    └── .github/
        └── workflows/
            └── deploy.yml                 # GitHub Actions workflow

Building Documentation
----------------------

To build the documentation locally:

.. code-block:: bash

    cd docs
    make clean
    make html

Then open the generated HTML:

.. code-block:: bash

    # macOS
    open _build/html/index.html

    # Linux
    xdg-open _build/html/index.html

    # Windows
    start _build/html/index.html

Dependencies
------------

Development dependencies are listed in ``requirements-dev.txt``:

- **Sphinx** (≥4.0.0): Documentation generator
- **myst-parser** (≥0.18.0): Markdown support for Sphinx
- **alabaster** (≥0.7.12): Clean HTML theme

Testing the Library
-------------------

To verify the library works correctly:

.. code-block:: python

    from mylib import Calculator, format_text, add_prefix

    # Test Calculator
    calc = Calculator()
    print(calc.add(5, 3))        # Output: 8
    print(calc.multiply(4, 2))   # Output: 8

    # Test Utils
    print(format_text("hello", uppercase=True))  # Output: HELLO
    print(add_prefix("world"))                    # Output: PREFIX_world

Troubleshooting
---------------

Import Error: ModuleNotFoundError
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

**Problem**: ``ModuleNotFoundError: No module named 'mylib'``

**Solution**:
Make sure you've installed the package in development mode:

.. code-block:: bash

    pip install -e .

Sphinx Build Error
^^^^^^^^^^^^^^^^^^^

**Problem**: ``sphinx: error: extension 'myst_parser' not found``

**Solution**:
Install the documentation dependencies:

.. code-block:: bash

    pip install -r requirements-dev.txt

Missing Static Files
^^^^^^^^^^^^^^^^^^^^

**Problem**: Documentation builds but CSS/images look broken

**Solution**:
Make sure the ``_static`` directory exists:

.. code-block:: bash

    mkdir -p docs/_static

Customization
-------------

Python Version
^^^^^^^^^^^^^^

The project supports Python 3.6+. To use a different version:

1. Create a virtual environment with that version
2. Activate it
3. Install dependencies

.. code-block:: bash

    python3.11 -m venv venv
    source venv/bin/activate
    pip install -r requirements-dev.txt

Documentation Theme
^^^^^^^^^^^^^^^^^^^^

To change the Sphinx theme, edit ``docs/conf.py``:

.. code-block:: python

    html_theme = 'alabaster'  # Change to 'sphinx_rtd_theme', 'press', etc.

Then rebuild the documentation.

Adding New Modules
^^^^^^^^^^^^^^^^^^^

To add a new module to the library:

1. Create a new file in ``mylib/``
2. Add functions with comprehensive docstrings
3. Export from ``mylib/__init__.py``
4. Create documentation in ``docs/api/``

See :doc:`Contributing <resources/contributing>` for details.

Development Workflow
--------------------

Typical workflow for development:

1. Create a branch: ``git checkout -b feature/my-feature``
2. Make changes to code or documentation
3. Build docs locally: ``cd docs && make html``
4. Review changes
5. Commit: ``git add . && git commit -m "message"``
6. Push: ``git push origin feature/my-feature``
7. Create a pull request on GitHub

Next Steps
----------

- :doc:`Getting Started <guides/getting_started>` with MyLib
- :doc:`Tutorial <guides/tutorial>` to build an application
- :doc:`Contributing <resources/contributing>` to the project
- :doc:`Deployment <deployment>` to GitHub Pages
