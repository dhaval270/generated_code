from typing import List

def below_zero(operations: List[int]) -> bool:
    """
    Detects if the balance of an account falls below zero at any point given a list of deposit and withdrawal operations.

    Args:
    operations (List[int]): A list of deposit and withdrawal operations. Positive values represent deposits, negative values represent withdrawals.

    Returns:
    bool: True if the balance falls below zero at any point, False otherwise.
    """
    balance = 0  # Initialize the balance to 0
    for operation in operations:  # Iterate over each operation
        balance += operation  # Update the balance
        if balance < 0:  # Check if the balance falls below 0
            return True  # If it does, return True immediately
    return False  # If the function completes without returning True, return False

# Test cases
print(below_zero([1, 2, 3]))  # False
print(below_zero([1, 2, -4, 5]))  # True
print(below_zero([]))  # False
print(below_zero([10, 20, 30]))  # False
print(below_zero([-10, -20, -30]))  # True