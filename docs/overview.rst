Overview
========

Welcome to the MyLib documentation site.

This site now includes:

- **A demo application** documented via Sphinx autodoc from the `demo_app` package
- **A library API reference** generated from the `mylib` package
- **Custom Markdown resources** under `/resources` exposed as individual pages
- **Project setup and deployment instructions** for GitHub Pages

Quick Links
-----------

- :doc:`Demo Application <app/index>` - Sphinx docs for the dummy app
  - Direct link: ``app/index.html``
- :doc:`Library API <api/index>` - Auto-generated Python API docs
- :doc:`Getting Started <guides/getting_started>` - User guide for using the project
- :doc:`Architecture <resources/architecture>` - System architecture notes
- :doc:`Best Practices <resources/best_practices>` - Development guidelines
- :doc:`Contributing <resources/contributing>` - Contribution instructions
- :doc:`Setup <setup>` - Local development setup
- :doc:`Deployment <deployment>` - GitHub Pages deployment guide

Project Overview
----------------

This repository includes two main codebases:

1. **`demo_app`** - A dummy application with its own docstrings and Sphinx autodoc support.
2. **`mylib`** - A utility library with a Calculator and text utilities.

The documentation site uses Sphinx to extract documentation from both source packages and to render custom Markdown content from `/resources`.

Installation
------------

.. code-block:: bash

    pip install -e .
    pip install -r requirements-dev.txt

Build Documentation Locally
---------------------------

.. code-block:: bash

    cd docs
    make clean
    make html
    open _build/html/index.html

Documentation Structure
-----------------------

**Demo Application**
- Sphinx-generated docs from `demo_app`
- Includes application flow, API references, and source-level docs

**Library API**
- Auto-generated documentation from `mylib`
- Includes `Calculator`, utilities, and API reference pages

**Resources**
- Markdown content from `/resources`
- Includes architecture, best practices, and contributing guides

**Project**
- Setup and deployment instructions

What You'll Find Here
---------------------

- A real demo application documented with Sphinx
- Source extraction of the application code
- Auto-generated library API docs
- Markdown resource pages in the left navigation
- A unified site with both app docs and library docs

Requirements
------------

- Python 3.6 or higher
- pip

Documentation dependencies:

- Sphinx >= 4.0.0
- myst-parser >= 0.18.0
- sphinx-rtd-theme >= 1.2.0

Navigation
----------

- Start at :doc:`Demo Application <app/index>` to explore the dummy app docs
- Browse :doc:`Library API <api/index>` for the code reference
- Use :doc:`Resources <resources/index>` for Markdown guides
- Follow :doc:`Setup <setup>` and :doc:`Deployment <deployment>` for local and site setup

Technology Stack
----------------

- **Python**
- **Sphinx**
- **MyST Parser**
- **sphinx_rtd_theme**
- **GitHub Actions**
- **GitHub Pages**

Project Structure
-----------------

.. code-block:: text

    gh-pages-ex/
    ├── demo_app/                 # Demo application package
    │   ├── __init__.py
    │   ├── app.py
    │   └── utils.py
    ├── mylib/                    # Python library package
    ├── docs/                     # Sphinx documentation source
    │   ├── conf.py
    │   ├── index.rst
    │   ├── overview.rst
    │   ├── app/
    │   ├── api/
    │   ├── guides/
    │   └── resources/
    ├── resources/                # Source Markdown docs
    ├── .github/workflows/
    └── setup.py

Support
-------

- Repo issues: https://github.com/yourusername/gh-pages-ex/issues
- Sphinx docs: https://www.sphinx-doc.org/
- MyST docs: https://myst-parser.readthedocs.io/

Ready to explore? Start with :doc:`Demo Application <app/index>` or :doc:`Library API <api/index>`.
