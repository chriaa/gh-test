Overview
========

MyLib is a simple Python library that showcases how to create comprehensive
documentation using Sphinx with both reStructuredText (RST) and Markdown formats.

Features
--------

- **Simple utility functions** for text processing
- **Core functionality** with a Calculator class for basic arithmetic
- **Sphinx integration** for professional documentation generation
- **MyST Parser support** enabling Markdown documentation writing
- **Multiple documentation sources** seamlessly integrated
- **Automatic API documentation** generated from docstrings
- **GitHub Pages deployment** via GitHub Actions

About This Project
------------------

MyLib demonstrates best practices for:

✅ Clean code structure with well-organized modules  
✅ Comprehensive docstrings for automatic API documentation  
✅ Sphinx integration for professional-grade documentation  
✅ MyST Parser support to write documentation in Markdown  
✅ Multiple documentation sources (code docs + custom guides)  
✅ GitHub Pages deployment for hosting documentation online  

Quick Links
-----------

- :doc:`Getting Started <guides/getting_started>` - Start using MyLib in 5 minutes
- :doc:`Tutorial <guides/tutorial>` - Build an application with MyLib
- :doc:`API Reference <api/index>` - Complete function and class reference
- :doc:`Resources <resources/index>` - Additional guides and documentation
- :doc:`Project Setup <setup>` - How to set up this project locally
- :doc:`Deployment <deployment>` - How to deploy documentation to GitHub Pages

Installation
------------

To use MyLib:

.. code-block:: bash

    pip install -e .

To work with the documentation:

.. code-block:: bash

    pip install -r requirements-dev.txt

Building Documentation Locally
-------------------------------

To build the documentation on your machine:

.. code-block:: bash

    cd docs
    make clean
    make html
    open _build/html/index.html

Documentation Structure
-----------------------

This documentation site contains:

**Guides** (Markdown)
    Getting started guide and comprehensive tutorials

**API Reference** (Auto-generated from code)
    Complete reference for all classes and functions

**Resources** (Markdown)
    Architecture overview, best practices, and contributing guidelines

**Project Information**
    Setup instructions and deployment guides

Technology Stack
----------------

- **Sphinx**: Documentation generator
- **MyST Parser**: Write Markdown in Sphinx
- **Alabaster**: Clean HTML theme
- **autodoc**: Auto-generate docs from docstrings
- **Napoleon**: Support for Google/NumPy style docstrings
- **GitHub Actions**: Automated documentation deployment

What's Next?
------------

1. Read the :doc:`Getting Started <guides/getting_started>` guide
2. Explore the :doc:`API Reference <api/index>`
3. Check out the :doc:`Tutorial <guides/tutorial>`
4. Review :doc:`Best Practices <resources/best_practices>`
5. Learn about :doc:`Architecture <resources/architecture>`
6. See how to :doc:`Contribute <resources/contributing>`
