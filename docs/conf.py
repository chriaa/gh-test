"""Sphinx configuration file for MyLib documentation."""

import os
import sys

# Add the parent directory to sys.path so we can import mylib
sys.path.insert(0, os.path.abspath('..'))

# Project information
project = 'MyLib'
copyright = '2026, Demo Author'
author = 'Demo Author'
release = '0.1.0'

# Sphinx extensions
extensions = [
    'sphinx.ext.autodoc',
    'sphinx.ext.napoleon',
    'sphinx.ext.viewcode',
    'myst_parser',
]

# MyST Parser configuration
myst_enable_extensions = [
    "colon_fence",
    "deflist",
]

# Source file formats
source_suffix = {
    '.rst': 'restructuredtext',
    '.md': 'markdown',
}

# Theme configuration
html_theme = 'alabaster'
html_static_path = ['_static']

# Autodoc settings
autodoc_member_order = 'bysource'
autodoc_typehints = 'description'

# Napoleon settings (for Google/NumPy style docstrings)
napoleon_google_docstring = True
napoleon_numpy_docstring = True
napoleon_include_init_with_doc = False
napoleon_include_private_with_doc = False
napoleon_include_special_with_doc = True
napoleon_use_admonition_for_examples = True
napoleon_use_admonition_for_notes = True
napoleon_use_admonition_for_references = False
napoleon_use_ivar = False
napoleon_use_param = True
napoleon_use_rtype = True
