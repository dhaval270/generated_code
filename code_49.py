from __future__ import annotations
from typing import List

def mean_absolute_deviation(numbers: List[float]) -> float:
    """
    For a given list of input numbers, calculate Mean Absolute Deviation
    around the mean of this dataset.

    Mean Absolute Deviation is the average absolute difference between each
    element and a centerpoint (mean in this case):
    MAD = average | x - x_mean |

    Parameters
    ----------
    numbers : List[float]
        A non‑empty list of numeric values.

    Returns
    -------
    float
        The mean absolute deviation of the input list.

    Raises
    ------
    ValueError
        If ``numbers`` is empty.

    Examples
    --------
    >>> mean_absolute_deviation([1.0, 2.0, 3.0, 4.0])
    1.0
    """
    if not numbers:
        raise ValueError("The input list must contain at least one number.")

    mean_val = sum(numbers) / len(numbers)
    total_abs_diff = sum(abs(x - mean_val) for x in numbers)
    return total_abs_diff / len(numbers)