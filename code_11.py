def has_close_elements(numbers: Sequence[Number], threshold: Number) -> bool:
    """
    Return ``True`` if any two numbers in *numbers* are closer to each other
    than *threshold*.

    Parameters
    ----------
    numbers : Sequence[Number]
        A sequence (list, tuple, etc.) of numeric values.
    threshold : Number
        The distance below which two numbers are considered “close”.
        Must be a non‑negative real number.

    Returns
    -------
    bool
        ``True`` if there exists a pair ``(x, y)`` in *numbers* such that
        ``abs(x - y) < threshold``; otherwise ``False``.

    Raises
    ------
    TypeError
        If *numbers* is not a sequence or contains non‑numeric items,
        or if *threshold* is not a real number.
    ValueError
        If *threshold* is negative.

    Notes
    -----
    * The function is **O(n log n)** because it sorts the input first.
    * Empty or single‑element sequences always return ``False``.
    * A threshold of ``0`` is allowed and will detect duplicate values.

    Examples
    --------
    >>> has_close_elements([1.0, 2.0, 3.0], 0.5)
    False
    >>> has_close_elements([1.0, 2.8, 3.0, 4.0, 5.0, 2.0], 0.3)
    True
    >>> has_close_elements([1, 1], 0)
    True
    """
    # ---------- Input validation ----------
    if not isinstance(numbers, Sequence):
        raise TypeError(f"'numbers' must be a sequence, got {type(numbers).__name__}")

    # Ensure threshold is a real number
    if not isinstance(threshold, (int, float)):
        raise TypeError(f"'threshold' must be a real number, got {type(threshold).__name__}")

    if threshold < 0:
        raise ValueError("threshold must be non‑negative")

    # Quick exit for