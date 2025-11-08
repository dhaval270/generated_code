from typing import List


def separate_paren_groups(paren_string: str) -> List[str]:
    """
    Split a string containing several balanced parenthesis groups into a list of
    those groups.  Spaces are ignored.

    Parameters
    ----------
    paren_string : str
        The input string.  It may contain spaces between parentheses and
        between groups.

    Returns
    -------
    List[str]
        A list of the balanced groups, in the order they appear.

    Examples
    --------
    >>> separate_paren_groups('( ) (( )) (( )( ))')
    ['()', '(())', '(()())']
    """
    groups: List[str] = []
    current: List[str] = []
    depth = 0

    for ch in paren_string:
        if ch == ' ':
            # ignore whitespace
            continue

        if ch not in ('(', ')'):
            # If the input may contain other characters, raise an error
            raise ValueError(f"Unexpected character: {ch!r}")

        # Update depth before or after adding the character?
        # We need to start a new group when depth goes from 0 to 1.
        if depth == 0 and ch == '(':
            current = []

        current.append(ch)

        # Update depth after appending the character
        if ch == '(':
            depth += 1
        else:  # ch == ')'
            depth -= 1

        # When depth returns to 0, we have a complete group
        if depth == 0:
            groups.append(''.join(current))

    if depth != 0:
        raise ValueError("Unbalanced parentheses in input")

    return groups