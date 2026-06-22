MyLib Documentation
===================

Welcome to the MyLib documentation! This project demonstrates how to create comprehensive
documentation using Sphinx with both reStructuredText (RST) and Markdown formats.

.. toctree::
   :maxdepth: 2
   :caption: Contents:

   overview
   guides/getting_started
   guides/tutorial
   app/index
   api/index
   resources/index

.. toctree::
   :maxdepth: 1
   :caption: Project:

   setup
   deployment

Demo Application and Library Docs
---------------------------------

This documentation site includes two main sections:

- **Demo Application**: View the dummy app docs in the `app` section.
- **Library API**: View the `mylib` reference in the `api` section.

The `Demo Application` section is available directly at:

- :doc:`Demo Application <app/index>`
- direct URL: ``app/index.html``

The left sidebar will show:

- Demo Application
  - Dummy Application
  - Demo App Utilities

If you are on the deployed site and you do not see the Demo Application section, the site may still be using an older deployment version.

- **Demo Application**: A custom application built for this project, documented with Sphinx autodoc and source code extraction.
- **Library API**: The `mylib` utility library with auto-generated API pages.

The **Resources** section contains your own Markdown documentation pages under `/resources`, exposed here as individual pages in the left navigation.

- **Clean code structure** with well-organized modules
- **Comprehensive docstrings** for automatic API documentation
- **Sphinx integration** for professional documentation
- **MyST Parser support** to write documentation in Markdown
- **Multiple documentation sources** seamlessly integrated

Features
--------

- Simple utility functions for text processing
- A Calculator class for basic arithmetic operations
- Full API documentation generated from docstrings
- Custom guides and tutorials written in Markdown

Quick Start
-----------

To get started with MyLib:

1. Install the package: ``pip install -e .``
2. Check the :doc:`Getting Started <guides/getting_started>` guide
3. Browse the :doc:`API Reference <api/index>`

Indices and tables
==================

* :ref:`genindex`
* :ref:`modindex`
* :ref:`search`
