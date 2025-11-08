from typing import List

def below_zero(operations: List[int]) -> bool:
    """
    Detects if the balance of a bank account falls below zero at any point.

    Args:
    operations (List[int]): A list of deposit and withdrawal operations on a bank account that starts with zero balance.
    
    Returns:
    bool: True if the balance falls below zero, False otherwise.

    Raises:
    TypeError: If the input is not a list.
    ValueError: If the list contains non-integer values.
    """

    # Check if input is a list
    if not isinstance(operations, list):
        raise TypeError("Input must be a list of integers.")

    # Check if all elements in the list are integers
    if not all(isinstance(op, int) for op in operations):
        raise ValueError("All elements in the list must be integers.")

    # Initialize balance to zero
    balance = 0

    # Iterate over each operation
    for op in operations:
        # Update balance
        balance += op

        # Check if balance falls below zero
        if balance < 0:
            return True

    # If balance never falls below zero, return False
    return False


# Example usage:
if __name__ == "__main__":
    print(below_zero([1, 2, 3]))  # False
    print(below_zero([1, 2, -4, 5]))  # True
    try:
        print(below_zero("not a list"))  # Raises TypeError
    except TypeError as e:
        print(e)
    try:
        print(below_zero([1, 2, "not an integer", 5]))  # Raises ValueError
    except ValueError as e:
        print(e)