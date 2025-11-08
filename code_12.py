from typing import List

def has_close_elements(numbers: List[float], threshold: float) -> bool:
    """
    Check if in given list of numbers, are any two numbers closer to each other than
    given threshold.

    Args:
        numbers (List[float]): A list of floating point numbers.
        threshold (float): The minimum distance between two numbers.

    Returns:
        bool: True if any two numbers are closer than the threshold, False otherwise.

    Raises:
        TypeError: If the input list is not a list or if the threshold is not a number.
        ValueError: If the input list is empty or if the threshold is negative.
    """

    # Check if the input is a list
    if not isinstance(numbers, list):
        raise TypeError("Input must be a list of numbers.")

    # Check if the list is not empty
    if len(numbers) == 0:
        raise ValueError("Input list cannot be empty.")

    # Check if all elements in the list are numbers
    if not all(isinstance(num, (int, float)) for num in numbers):
        raise TypeError("All elements in the list must be numbers.")

    # Check if the threshold is a number
    if not isinstance(threshold, (int, float)):
        raise TypeError("Threshold must be a number.")

    # Check if the threshold is non-negative
    if threshold < 0:
        raise ValueError("Threshold cannot be negative.")

    # Sort the list of numbers
    numbers.sort()

    # Iterate over the sorted list to check for close elements
    for i in range(len(numbers) - 1):
        if numbers[i + 1] - numbers[i] <= threshold:
            return True

    # If no close elements are found, return False
    return False


# Example usage:
if __name__ == "__main__":
    print(has_close_elements([1.0, 2.0, 3.0], 0.5))  # False
    print(has_close_elements([1.0, 2.8, 3.0, 4.0, 5.0, 2.0], 0.3))  # True