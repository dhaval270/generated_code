from typing import List


def below_zero(operations: List[int]) -> bool:
    """
    Detect whether a bank account balance ever falls below zero.

    The account starts at a balance of zero. Each element in `operations`
    represents a deposit (positive integer) or a withdrawal (negative integer).
    As soon as the running balance becomes negative, the function returns
    ``True``. If the balance never goes below zero, ``False`` is returned.

    Parameters
    ----------
    operations : List[int]
        A list of integers representing successive deposits and withdrawals.

    Returns
    -------
    bool
        ``True`` if the balance ever becomes negative, otherwise ``False``.

    Examples
    --------
    >>> below_zero([1, 2, 3])
    False
    >>> below_zero([1, 2, -4, 5])
    True
    >>> below_zero([])
    False
    >>> below_zero([-1, 5, -10])
    True
    """
    balance = 0
    for op in operations:
        balance += op
        if balance < 0:
            return True
    return False