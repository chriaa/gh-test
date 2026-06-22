"""Main application module for the demo app."""

from .utils import normalize_text, calculate_word_stats


class DummyApp:
    """A minimal demo application that processes text input.

    The DummyApp is designed to demonstrate Sphinx autodoc extraction from
    real source code. It exposes a simple workflow for text normalization,
    prefixing, and summary statistics.
    """

    def __init__(self, text=""):
        """Initialize the application with optional initial text."""
        self.text = text
        self.history = []

    def set_text(self, text):
        """Set the application's current text.

        Args:
            text (str): Text to process.

        Returns:
            DummyApp: Self, for method chaining.
        """
        self.text = text
        self.history.append(("set_text", text))
        return self

    def normalize(self):
        """Normalize the current text using utility helpers.

        Returns:
            DummyApp: Self, for method chaining.
        """
        self.text = normalize_text(self.text)
        self.history.append(("normalize", self.text))
        return self

    def summarize(self):
        """Compute summary statistics for the current text.

        Returns:
            dict: A dictionary containing word count and average word length.
        """
        stats = calculate_word_stats(self.text)
        self.history.append(("summarize", stats))
        return stats

    def add_prefix(self, prefix="DEMO"):
        """Add a prefix to the current text.

        Args:
            prefix (str): Prefix string to add.

        Returns:
            DummyApp: Self, for method chaining.
        """
        self.text = f"{prefix}_{self.text}"
        self.history.append(("add_prefix", prefix))
        return self

    def clear(self):
        """Clear the current text and history."""
        self.text = ""
        self.history.clear()
        return self
