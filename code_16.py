from typing import List

def separate_paren_groups(paren_string: str) -> List[str]:
    """
    Separate groups of nested parentheses in a string into individual strings.

    Args:
    paren_string (str): Input string containing multiple groups of nested parentheses.

    Returns:
    List[str]: List of strings, each representing a separate group of parentheses.
    """
    # Remove spaces from the input string
    paren_string = paren_string.replace(' ', '')

    # Initialize an empty list to store the separated groups
    groups = []

    # Initialize an empty stack to keep track of the current group
    stack = []

    # Initialize an empty string to build the current group
    current_group = ''

    # Iterate over each character in the input string
    for char in paren_string:
        # If the character is an open parenthesis, push it onto the stack and add it to the current group
        if char == '(':
            stack.append(char)
            current_group += char
        # If the character is a close parenthesis, pop the corresponding open parenthesis from the stack and add the close parenthesis to the current group
        elif char == ')':
            if not stack:
                raise ValueError("Unbalanced parentheses in input string")
            stack.pop()
            current_group += char
            # If the stack is empty after popping, it means we've found a complete group, so add it to the list of groups and reset the current group
            if not stack:
                groups.append(current_group)
                current_group = ''

    # If there are any remaining characters in the current group, it means the input string had unbalanced parentheses, so raise an error
    if current_group:
        raise ValueError("Unbalanced parentheses in input string")

    return groups

# Example usage:
print(separate_paren_groups('( ) (( )) (( )( ))'))  # Output: ['()', '(())', '(()())']