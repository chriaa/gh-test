"""Utility functions used by the demo application."""


def normalize_text(text):
    """Normalize text by trimming whitespace and lowercasing.

    Args:
        text (str): The input string to normalize.

    Returns:
        str: The normalized string.
    """
    return text.strip().lower()


def calculate_word_stats(text):
    """Calculate summary statistics for the given text.

    Args:
        text (str): The input text.

    Returns:
        dict: A dictionary with word count and average word length.
    """
    words = [word for word in text.split() if word]
    word_count = len(words)
    if word_count == 0:
        return {"word_count": 0, "average_length": 0.0}

    average_length = sum(len(word) for word in words) / word_count
    return {"word_count": word_count, "average_length": average_length}
