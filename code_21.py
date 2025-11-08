from __future__ import annotations

from typing import List


def separate_paren_groups(paren_string: str) -> List[str]:
    """
    Split a string that contains several *non‑overlapping* groups of balanced
    parentheses into a list of those groups.

    The input may contain arbitrary whitespace – it is ignored.  Each group
    is guaranteed to be balanced and the groups are not nested inside one
    another.

    Parameters
    ----------
    paren_string : str
        The raw string containing the parentheses and optional spaces.

    Returns
    -------
    List[str]
        A list of the individual parenthesis groups, in the order they appear
        in the input.

    Examples
    --------
    >>> separate_paren_groups('( ) (( )) (( )( ))')
    ['()', '(())', '(()())']

    >>> separate_paren_groups('((())) ()')
    ['((()))', '()']

    >>> separate_paren_groups('   (  )   ')
    ['()']
    """
    # Remove all whitespace – it is irrelevant for the grouping logic.
    cleaned = paren_string.replace(" ", "")

    groups: List[str] = []
    current: List[str] = []
    depth = 0

    for ch in cleaned:
        if ch == "(":
            depth += 1
        elif ch == ")":
            depth -= 1
        else:
            # The problem guarantees that only parentheses appear after
            # whitespace removal, but we guard against unexpected chars.
            raise ValueError(f"Unexpected character {ch!r} in input")

        current.append(ch)

        # When depth returns to zero we have closed a complete group.
        if depth == 0:
            groups.append("".join(current))
            current.clear()

    # If the input is guaranteed to be balanced, we should never reach here
    # with a non‑empty current list.  The guard is kept for safety.
    if current:
        raise ValueError("Unbalanced parentheses in input")

    return groups