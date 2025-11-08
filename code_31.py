import math
from typing import Union

def truncate_number(number: Union[float, int]) -> float:
    """
    Return the decimal (fractional) part of a non‑negative floating‑point number.

    The function works for both ``float`` and ``int`` inputs.  For an integer
    input the fractional part is ``0.0``.  If a negative value is supplied a
    ``ValueError`` is raised – the original docstring explicitly mentions
    *positive* numbers, so we guard against accidental misuse.

    Parameters
    ----------
    number : float | int
        The number to truncate.  Must be non‑negative.

    Returns
    -------
    float
        The fractional part of ``number`` (always in the range ``[0, 1)``).

    Examples
    --------
    >>> truncate_number(3.5)
    0.5
    >>> truncate_number(10)
    0.0
    >>> truncate_number(0.123456)
    0.123456
    """
    if number < 0:
        raise ValueError("truncate_number expects a non‑negative number")

    # ``math.modf`` returns a tuple (fractional, integer) with the same sign
    # as the input.  For non‑negative numbers the fractional part is exactly
    # what we want.
    fractional, _ = math.modf(float(number))
    return fractional