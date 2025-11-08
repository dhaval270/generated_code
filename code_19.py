from typing import List


def separate_paren_groups(paren_string: str) -> List[str]:
    """
    Split a string containing several top‑level parenthesis groups into a list of those groups.

    The input may contain arbitrary spaces which are ignored.  Each group is a balanced
    parenthesis expression that is not nested inside another group.

    Parameters
    ----------
    paren_string : str
        The string to parse.

    Returns
    -------
    List[str]
        A list of the top‑level parenthesis groups, in the order they appear.

    Examples
    --------
    >>> separate_paren_groups('( ) (( )) (( )( ))')
    ['()', '(())', '(()())']
    """
    groups: List[str] = []
    depth = 0          # current nesting depth
    start_index = None  # index where the current group starts

    for i, ch in enumerate(paren_string):
        if ch == ' ':
            continue  # ignore spaces

        if ch == '(':
            if depth == 0:
                # start of a new top‑level group
                start_index = i
            depth += 1
        elif ch == ')':
            depth -= 1
            if depth == 0 and start_index is not None:
                # end of a top‑level group
                groups.append(paren_string[start_index:i + 1])
                start_index = None
        else:
            # any other character is considered invalid for this problem
            # but we simply ignore it to keep the function robust
            continue

    return groups