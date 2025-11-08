from typing import List


def below_zero(operations: List[int]) -> bool:
    """
    Return True if the running balance ever becomes negative.

    The account starts at a balance of 0.  Each element in *operations* is
    applied in order: a positive number is a deposit, a negative number is a
    withdrawal.  As soon as the balance falls below zero the function returns
    True; otherwise it returns False after all operations have been processed.

    Parameters
    ----------
    operations : List[int]
        Sequence of integer deposits/withdrawals.

    Returns
    -------
    bool
        True if the balance ever goes negative, False otherwise.

    Examples
    --------
    >>> below_zero([1, 2, 3])
    False
    >>> below_zero([1, 2, -4, 5])
    True
    """
    balance = 0
    for op in operations:
        balance += op
        if balance < 0:
            return True
    return False