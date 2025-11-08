from typing import List


def below_zero(operations: List[int]) -> bool:
    """
    Detect whether a bank account ever goes below zero.

    The account starts with a balance of 0. Each element in *operations* is a
    deposit (positive) or withdrawal (negative).  If at any point the balance
    becomes negative, the function returns ``True``; otherwise it returns
    ``False``.

    Parameters
    ----------
    operations : List[int]
        A list of integers representing deposits (+) and withdrawals (-).

    Returns
    -------
    bool
        ``True`` if the balance ever falls below zero, otherwise ``False``.

    Examples
    --------
    >>> below_zero([1, 2, 3])
    False
    >>> below_zero([1, 2, -4, 5])
    True
    >>> below_zero([])
    False
    >>> below_zero([-1, 2, -3])
    True
    """
    balance = 0
    for op in operations:
        balance += op
        if balance < 0:
            return True
    return False


if __name__ == "__main__":
    import doctest
    doctest.testmod()