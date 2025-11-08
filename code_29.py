def truncate_number(number: float) -> float:
    """
    Return the decimal (fractional) part of a positive floating‑point number.

    The function decomposes ``number`` into an integer part (the largest
    integer not greater than ``number``) and a fractional part that is
    always in the interval ``[0, 1)``.

    Parameters
    ----------
    number : float
        A positive, finite floating‑point number.

    Returns
    -------
    float
        The fractional part of ``number``.  For an exact integer the
        result is ``0.0``.

    Raises
    ------
    ValueError
        If ``number`` is negative, NaN, or infinite.

    Examples
    --------
    >>> truncate_number(3.5)
