from typing import List

def below_zero(operations: List[int]) -> bool:
    """Detects if the balance of an account falls below zero at any point during a series of operations."""
    
    # Initialize the balance to zero
    balance = 0
    
    # Iterate through each operation
    for operation in operations:
        # Update the balance based on the operation
        balance += operation
        
        # Check if the balance has fallen below zero
        if balance < 0:
            # If it has, return True immediately
            return True
    
    # If we've completed all operations without the balance falling below zero, return False
    return False

# Example usage:
print(below_zero([1, 2, 3]))  # False
print(below_zero([1, 2, -4, 5]))  # True