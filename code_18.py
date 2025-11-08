from typing import List

def separate_paren_groups(paren_string: str) -> List[str]:
    """
    Separate groups of nested parentheses into separate strings.

    Args:
    paren_string (str): A string containing multiple groups of nested parentheses.

    Returns:
    List[str]: A list of strings, each representing a separate group of parentheses.

    Raises:
    ValueError: If the input string is not balanced.
    """
    # Remove spaces from the input string
    paren_string = paren_string.replace(" ", "")

    # Initialize the stack, list of groups, and current group
    stack = []
    groups = []
    current_group = ""

    # Iterate over each character in the string
    for char in paren_string:
        # If the character is an opening parenthesis, push it onto the stack and add it to the current group
        if char == "(":
            stack.append(char)
            current_group += char
        # If the character is a closing parenthesis, pop the corresponding opening parenthesis from the stack and add the closing parenthesis to the current group
        elif char == ")":
            if not stack:
                raise ValueError("Unbalanced parentheses")
            stack.pop()
            current_group += char
            # If the stack is empty after popping, it means we have found a complete group, so add it to the list of groups and reset the current group
            if not stack:
                groups.append(current_group)
                current_group = ""

    # If there are still characters in the current group, it means the string is not balanced, so raise an error
    if current_group:
        raise ValueError("Unbalanced parentheses")

    return groups

# Example usage
print(separate_paren_groups('( ) (( )) (( )( ))'))  # Output: ['()', '(())', '(()())']