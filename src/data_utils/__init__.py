"""Data utilities module."""

def clean_data(data: list) -> list:
    """Clean list by removing None and empty strings."""
    return [item for item in data if item is not None and item != ""]

def average(numbers: list) -> float:
    """Calculate average of a list of numbers."""
    if not numbers:
        return 0.0
    return sum(numbers) / len(numbers)

# Simple data utils mini project