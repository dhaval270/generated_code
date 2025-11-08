import math
from typing import Final

__all__: Final = ["truncate_number"]


def truncate_number(number: float) -> float:
    """
    Return the fractional (decimal) part of a positive floating‑point number.

    The function works by subtracting the largest integer not greater than
    ``number`` from the number itself.  For positive values this is simply
    ``number - math.floor(number)``.  The implementation uses ``math.floor``
    instead of ``int`` to avoid the subtle truncation behaviour of ``int``
    for negative numbers and to make the intent explicit.

    Parameters
    ----------
    number : float
        A positive floating‑point number.

    Returns
    -------
    float
        The fractional part of ``number`` (always in the range ``[0, 1)``).

    Raises
    ------
    ValueError
        If ``number`` is negative.

    Examples
    --------
    >>> truncate_number(3.5)
    0.5
    >>> truncate_number(10.0)
    0.0
    >>> truncate_number(0.123456)
    0.123456
    """
    if number < 0:
        raise ValueError("truncate_number expects a non‑negative number")

    # Subtract the integer part to isolate the fractional part.
    return number - math.floor(number)


# --------------------------------------------------------------------------- #
# Optional: simple test harness (not required for the function itself)
# --------------------------------------------------------------------------- #
if __name__ == "__main__":
    import doctest
    doctest.testmod()