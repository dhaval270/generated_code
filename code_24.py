from typing import List

def separate_paren_groups(paren_string: str) -> List[str]:
    """
    This function separates groups of nested parentheses in a given string into separate strings.
    
    Args:
        paren_string (str): A string containing multiple groups of nested parentheses.
    
    Returns:
        List[str]: A list of strings, each representing a separate group of balanced parentheses.
    
    Raises:
        ValueError: If the input string contains unbalanced parentheses.
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
        # If the character is a closing parenthesis, check if the stack is empty
        elif char == ")":
            # If the stack is empty, raise a ValueError because there's no matching opening parenthesis
            if not stack:
                raise ValueError("Unbalanced parentheses in the input string")
            # If the stack is not empty, pop the opening parenthesis from the stack and add the closing parenthesis to the current group
            else:
                stack.pop()
                current_group += char
                # If the stack is empty after popping, it means we've found a complete group, so add it to the list of groups and reset the current group
                if not stack:
                    groups.append(current_group)
                    current_group = ""
    
    # If the stack is not empty after iterating over the entire string, raise a ValueError because there are unbalanced opening parentheses
    if stack:
        raise ValueError("Unbalanced parentheses in the input string")
    
    return groups

# Example usage:
print(separate_paren_groups('( ) (( )) (( )( ))'))  # Output: ['()', '(())', '(()())']