from typing import List


def below_zero(operations: List[int]) -> bool:
    """
    Return True if the account balance ever drops below zero.

    The account starts at a balance of 0. Each integer in *operations* is
    applied sequentially: a positive value is a deposit, a negative value
    is a withdrawal.  As soon as the running total becomes negative the
    function returns True; otherwise it returns False after all
    operations have been processed.

    Examples
    --------
    >>> below_zero([1, 2, 3])
    False
    >>> below_zero([1, 2, -4, 5])
    True
    """
    balance = 0
    for amount in operations:
        balance += amount
        if balance < 0:
            return True
    return False


# Optional: quick manual test when run as a script
if __name__ == "__main__":
    import doctest
    doctest.testmod()