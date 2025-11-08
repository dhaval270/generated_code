from typing import List


def below_zero(operations: List[int]) -> bool:
    """
    Determine whether a bank account ever goes negative.

    The account starts with a balance of zero. Each element in *operations*
    represents a deposit (positive value) or a withdrawal (negative value).
    The function returns ``True`` as soon as the balance drops below zero,
    otherwise it returns ``False`` after processing all operations.

    Parameters
    ----------
    operations : List[int]
        A list of integers representing successive deposits and withdrawals.

    Returns
    -------
    bool
        ``True`` if the balance ever becomes negative, ``False`` otherwise.

    Examples
    --------
    >>> below_zero([1, 2, 3])
    False
    >>> below_zero([1, 2, -4, 5])
    True
    >>> below_zero([])
    False
    """
    balance = 0
    for amount in operations:
        balance += amount
        if balance < 0:
            return True
    return False