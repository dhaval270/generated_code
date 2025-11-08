from __future__ import annotations

import math
from typing import Union

Number = Union[int, float]


def truncate_number(number: Number) -> float:
    """
    Return the fractional (decimal) part of a *positive* floating‑point number.

    The function accepts ``int`` or ``float`` values.  For negative numbers
    a :class:`ValueError` is raised because the original specification
    explicitly mentions *positive* numbers.  Non‑numeric inputs raise
    :class:`TypeError`.

    Parameters
    ----------
    number : int | float
        The number to truncate.

    Returns
    -------
    float
        The fractional part of ``number`` (always in the range ``[0, 1)``).

    Raises
    ------
    TypeError
        If ``number`` is not an ``int`` or ``float``.
    ValueError
        If ``number`` is negative.

    Examples
    --------
    >>> truncate_number(3.5)
    0.5
    >>> truncate_number(10)
    0.0
    >>> truncate_number(0.9999)
    0.9999
    >>> truncate_number(-1.2)
    Traceback (most recent call last):
        ...
    ValueError: number must be non‑negative
    >>> truncate_number("3.5")
    Traceback (most recent call last):
        ...
    TypeError: number must be an int or float
    """
    # --- Input validation ----------------------------------------------------
    if not isinstance(number, (int, float)):
        raise TypeError("number must be an int or float")

    if number < 0:
        raise ValueError("number must be non‑negative")

    # --- Core logic ----------------------------------------------------------
    # ``math.modf`` returns a tuple (fractional, integer) for floats.
    # For ints it returns (0.0, number).  We cast to float to keep the
    # return type consistent.
    fractional, _ = math.modf(float(number))
    return float(fractional)


# --------------------------------------------------------------------------- #
# Optional: simple test harness (uncomment to run manually)
# --------------------------------------------------------------------------- #
if __name__ == "__main__":
    import doctest
    doctest.testmod()