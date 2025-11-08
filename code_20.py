from typing import List

def separate_paren_groups(paren_string: str) -> List[str]:
    """
    Separate groups of balanced parentheses in a string into separate strings.

    Args:
    paren_string (str): Input string containing multiple groups of nested parentheses.

    Returns:
    List[str]: List of strings, each representing a separate group of balanced parentheses.
    """
    # Remove spaces from the input string
    paren_string = paren_string.replace(" ", "")

    # Initialize an empty list to store the separated groups
    groups = []

    # Initialize an empty stack to keep track of the opening parentheses
    stack = []

    # Initialize an empty string to build the current group
    current_group = ""

    # Iterate over each character in the input string
    for char in paren_string:
        # If the character is an opening parenthesis, push it onto the stack and add it to the current group
        if char == "(":
            stack.append(char)
            current_group += char
        # If the character is a closing parenthesis, pop the corresponding opening parenthesis from the stack
        # and add the closing parenthesis to the current group
        elif char == ")":
            stack.pop()
            current_group += char
            # If the stack is empty after popping, it means we've found a complete group
            if not stack:
                groups.append(current_group)
                current_group = ""

    return groups

# Example usage:
print(separate_paren_groups('( ) (( )) (( )( ))'))  # Output: ['()', '(())', '(()())']