"""Demo application package for Sphinx documentation extraction."""

from .app import DummyApp
from .utils import normalize_text, calculate_word_stats

__all__ = ["DummyApp", "normalize_text", "calculate_word_stats"]

__version__ = "0.1.0"
