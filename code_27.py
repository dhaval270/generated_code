def truncate_number(number: Union[int, float]) -> float:
    """
    Return the fractional (decimal) part of a positive floating‑point number.

    The function decomposes ``number`` into its integer part and its fractional
    part.  The fractional part is always a value in the interval ``[0, 1)``.
    For integer inputs the result is ``0.0``.

    Parameters
    ----------
    number : int | float
        A non‑negative number.  The function accepts ``int`` as well as
        ``float`` for convenience.

    Returns
    -------
    float
        The decimal part of ``number``.  For example::

            >>> truncate_number(3.5)
            0.5
            >>> truncate_number(7)
            0.0

    Notes
    -----
    * The implementation uses :func:`math.modf`, which returns the fractional
      part and the integer part of a number.  ``math.modf`` handles the
      floating‑point quirks of Python and keeps the sign of the input.
    * Although the problem statement says the input is positive, the
      implementation works for negative numbers as well, returning a negative
      fractional part (e.g. ``truncate_number(-2.3)`` → ``-0.3``).  If you
      want to enforce positivity, you can add an explicit check.

    Examples
    --------
    >>> truncate_number(3.5)
    0.5
    >>> truncate_number(10.999)
    0.999
    >>> truncate_number(0)
    0.0
    """
    # ``math.modf`` returns