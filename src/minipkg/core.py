def add(a: int, b: int) -> int:
    """A tiny example function."""
    if a < 0 or b < 0:
        raise ValueError("Negative values not allowed")
    return a + b
