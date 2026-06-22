"""
MyLib - A simple Python library for demonstration purposes.

This library showcases how to create comprehensive documentation
using Sphinx with both RST and Markdown formats.
"""

__version__ = "0.1.0"
__author__ = "Demo Author"

from .core import Calculator
from .utils import format_text, add_prefix

__all__ = ["Calculator", "format_text", "add_prefix"]
