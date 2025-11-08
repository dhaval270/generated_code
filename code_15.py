from typing import List


def separate_paren_groups(paren_string: str) -> List[str]:
    """
    Split a string that contains several balanced parenthesis groups into a list of
    those groups.  Spaces are ignored.

    Parameters
    ----------
    paren_string : str
        A string that may contain '(' , ')' and whitespace.  The string is
        guaranteed to contain only balanced groups that are not nested inside
        each other.

    Returns
    -------
    List[str]
        A list of the individual balanced groups, in the order they appear.

    Examples
    --------
    >>> separate_paren_groups('( ) (( )) (( )( ))')
    ['()', '(())', '(()())']

    >>> separate_paren_groups('((())) ()')
    ['((()))', '()']

    >>> separate_paren_groups('   ')
    []

    >>> separate_paren_groups('()((()))')
    ['()', '((()))']
    """
    groups: List[str] = []
    current: List[str] = []
    depth = 0

    for ch in paren_string:
        if ch == ' ':
            continue  # ignore whitespace

        if ch == '(':
            if depth == 0:
                current = []          # start a new group
            depth += 1
            current.append(ch)

        elif ch == ')':
            depth -= 1
            current.append(ch)
            if depth == 0:
                groups.append(''.join(current))  # close the group

        else:
            # If other characters appear we simply ignore them.
            # The problem statement guarantees only parentheses and spaces.
            continue

    return groups