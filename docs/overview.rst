Welcome to MyLib
================

A simple Python library demonstrating professional documentation practices with Sphinx, MyST, and GitHub Pages.

**MyLib** is a sample Python library that showcases how to create comprehensive documentation. It demonstrates clean code organization, professional API documentation, and modern deployment practices.

Quick Start
-----------

Installation
^^^^^^^^^^^^

.. code-block:: bash

    pip install -e .

Basic Usage
^^^^^^^^^^^

**Using the Calculator:**

.. code-block:: python

    from mylib import Calculator
    
    calc = Calculator()
    result = calc.add(10, 5)      # 15
    result = calc.multiply(4, 2)  # 8
    result = calc.divide(20, 4)   # 5.0

**Using Text Utilities:**

.. code-block:: python

    from mylib import format_text, add_prefix
    
    text = format_text("hello", uppercase=True)  # "HELLO"
    prefixed = add_prefix("world")               # "PREFIX_world"

Build Documentation Locally
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. code-block:: bash

    pip install -r requirements-dev.txt
    cd docs
    make clean
    make html
    open _build/html/index.html

Documentation Sections
----------------------

**📖 Guides** - Getting Started & Tutorial
    Start here to learn how to use MyLib:
    
    - :doc:`Getting Started <guides/getting_started>` - 5-minute introduction
    - :doc:`Tutorial <guides/tutorial>` - Build an application with MyLib

**🔧 API Reference** - Complete Function & Class Documentation
    Detailed reference for all modules:
    
    - :doc:`Core Module <api/core>` - Calculator class
    - :doc:`Utils Module <api/utils>` - Text utilities

**📚 Resources** - Architecture & Best Practices
    Learn about the project structure and guidelines:
    
    - :doc:`Architecture <resources/architecture>` - System design
    - :doc:`Best Practices <resources/best_practices>` - Development guidelines
    - :doc:`Contributing <resources/contributing>` - How to contribute

**📋 Project** - Setup & Deployment
    Local development and production deployment:
    
    - :doc:`Setup <setup>` - Local development setup
    - :doc:`Deployment <deployment>` - Deploy to GitHub Pages

Key Features
------------

✅ **Professional Grade** - Production-ready code structure  
✅ **Well Documented** - Every function has comprehensive docstrings  
✅ **Multiple Formats** - Mix Markdown and reStructuredText  
✅ **Auto-Generated API** - Documentation from code docstrings  
✅ **GitHub Pages Ready** - One-click deployment with GitHub Actions  
✅ **Best Practices** - Demonstrates Python and documentation standards  

What You'll Find Here
---------------------

This documentation site includes:

1. **Complete API Reference** (auto-generated from Python docstrings)
2. **Getting Started Guide** (quick introduction to MyLib)
3. **Comprehensive Tutorial** (build a real application)
4. **Best Practices Guide** (development guidelines)
5. **Architecture Overview** (system design and structure)
6. **Contributing Guidelines** (how to contribute)
7. **Setup Instructions** (local development)
8. **Deployment Guide** (GitHub Pages with GitHub Actions)

Requirements
------------

- Python 3.6 or higher
- pip (Python package manager)

For documentation:

- Sphinx >= 4.0.0
- myst-parser >= 0.18.0
- alabaster >= 0.7.12

Quick Install
^^^^^^^^^^^^^

.. code-block:: bash

    # Install dependencies
    pip install -r requirements-dev.txt
    
    # Install the package
    pip install -e .

Navigation
----------

**First Time Here?**
    Start with :doc:`Getting Started <guides/getting_started>`

**Want to Use MyLib?**
    Read the :doc:`Tutorial <guides/tutorial>`

**Looking for API Details?**
    See :doc:`Core Module <api/core>` or :doc:`Utils Module <api/utils>`

**Contributing to the Project?**
    Check :doc:`Contributing <resources/contributing>`

**Setting Up Locally?**
    Follow :doc:`Setup <setup>`

**Deploying Docs?**
    Read :doc:`Deployment <deployment>`

Technology Stack
----------------

- **Python 3.6+** - Programming language
- **Sphinx** - Documentation generator
- **MyST Parser** - Markdown support for Sphinx
- **Alabaster** - Clean, professional theme
- **GitHub Actions** - CI/CD and deployment
- **GitHub Pages** - Documentation hosting

Project Structure
-----------------

.. code-block:: text

    gh-pages-ex/
    ├── mylib/                    # Python library
    │   ├── __init__.py
    │   ├── core.py               # Calculator class
    │   └── utils.py              # Text utilities
    ├── docs/                     # Sphinx documentation
    │   ├── conf.py
    │   ├── index.rst
    │   ├── overview.rst          # This page
    │   ├── api/                  # API documentation
    │   ├── guides/               # User guides
    │   └── resources/            # Resources (auto-copied)
    ├── resources/                # Source markdown files
    ├── .github/workflows/        # GitHub Actions
    └── setup.py                  # Package setup

Support & Resources
-------------------

- **Repository**: https://github.com/yourusername/gh-pages-ex
- **Issues**: Report bugs on GitHub Issues
- **Sphinx Documentation**: https://www.sphinx-doc.org/
- **MyST Parser**: https://myst-parser.readthedocs.io/
- **GitHub Pages**: https://docs.github.com/en/pages

---

Ready to dive in? Start with the :doc:`Getting Started <guides/getting_started>` guide or explore the :doc:`API Reference <api/index>`!
