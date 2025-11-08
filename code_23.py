def separate_paren_groups(paren_string: str) -> List[str]:
    """
    Split a string that contains several *top‑level* groups of balanced parentheses
    into a list of those groups.

    The function ignores all whitespace characters.  A group is defined as a
    contiguous sequence of parentheses that starts with an opening ``(`` and ends
    with the matching closing ``)`` at depth zero.  Groups are **not** nested
    inside one another – the input is assumed to be a sequence of independent
    balanced expressions.

    Parameters
    ----------
    paren_string : str
        The raw input string.  It may contain spaces, tabs, newlines, etc.
        These are ignored.

    Returns
    -------
    List[str]
        A list of strings, each string being a balanced group of parentheses
        (including the outermost ``(`` and ``)``).

    Raises
    ------
    ValueError
        If the input contains unmatched parentheses, or if a closing parenthesis
        appears before an opening one.

    Examples
    --------
    >>> separate_paren_groups('( ) (( )) (( )( ))')
    ['()', '(())', '(()())']

    >>> separate_paren_groups('((()))')
    ['((()))']

    >>> separate_paren_groups('()()')
    ['()', '()']

    >>> separate_paren_groups('(()')
    Traceback (most recent call last):
        ...
    ValueError: Unbalanced parentheses – missing closing ')'.

    >>> separate_paren_groups(')(')
    Traceback (most recent call last):
        ...
    ValueError: Unbalanced parentheses – closing ')' without matching '('.
    """
    if not isinstance(paren_string, str):
        raise TypeError(f"Expected a string, got {type(paren_string).__name__}")

    # Remove all whitespace – this keeps the logic simple
    cleaned = "".join(ch for ch in paren_string if not ch.isspace())

    groups: List[str] = []
    depth = 0
    current_start: int | None = None

    for idx, ch in enumerate(cleaned):
        if ch == "(":
            if depth == 0:
                # start of a new group
                current_start = idx
            depth += 1
        elif ch == ")":
            depth -= 1
            if depth < 0:
                # more closing than opening
                raise ValueError(
                    f"Unbalanced parentheses – closing ')' at position {idx} "
                    f"without matching '('."
                )
            if depth == 0:
                # end of a group
                if current_start is None:
                    # this should never happen because depth==0 implies we had a start
                    raise RuntimeError("Internal error: depth reached 0 without a start index.")
                groups.append(cleaned[current_start : idx + 1])
                current_start = None
        else:
            # Any other character is considered an