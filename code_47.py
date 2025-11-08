def below_zero(operations: Sequence[Number]) -> bool:
    """
    Return ``True`` if the running balance ever falls below zero.

    The account starts at a balance of zero.  Each element of *operations*
    represents a deposit (positive) or withdrawal (negative).  As soon as
    the cumulative sum becomes negative the function returns ``True``.
    If the balance never goes negative the function returns ``False``.

    Parameters
    ----------
    operations : Sequence[Number]
        A sequence of numeric values.  Each value must be an ``int`` or a
        ``float`` that represents an integer (e.g. ``1.0`` is accepted).

    Returns
    -------
    bool
        ``True`` if the balance ever becomes negative, otherwise ``False``.

    Raises
    ------
    TypeError
        If *operations* is not a sequence, or if any element is not a
        numeric type or is a non‑integral float.

    Examples
    --------
    >>> below_zero([1, 2, 3])
    False
    >>> below_zero([1, 2, -4, 5])
    True
    >>> below_zero([])
    False
    >>> below_zero([1, 2, 'a'])
    Traceback (most recent call last):
        ...
    TypeError: All elements of operations must be int or float representing an integer.
    """
    # Basic type checks
    if not isinstance(operations, Sequence):
        raise TypeError("operations must be a sequence (list, tuple, etc.)")

    balance = 0
    for idx, op in enumerate(operations):
        # Validate each element
        if isinstance(op, int):
            value = op
        elif isinstance(op, float):
            if not op.is_integer():
                raise TypeError(
                    f"Element at index {idx} is a non‑integral float: {op!r}"
                )
            value = int(op)
        else:
            raise TypeError(
                f"Element at index {idx} is not a number: {op!r}"
            )

        balance += value
        if balance < 0:
            return True

    return False

