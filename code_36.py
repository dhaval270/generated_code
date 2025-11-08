def truncate_number(number: float) -> float:
    """
    Given a positive floating point number, it can be decomposed into
    an integer part (largest integer smaller than given number) and decimals
    (leftover part always smaller than 1).

    Return the decimal part of the number.

    Args:
        number (float): A positive floating point number.

    Returns:
        float: The decimal part of the number.

    Raises:
        TypeError: If the input is not a float.
        ValueError: If the input is not a positive number.
    """

    # Check if the input is a float
    if not isinstance(number, (int, float)):
        raise TypeError("Input must be a float or an integer.")

    # Check if the input is a positive number
    if number < 0:
        raise ValueError("Input must be a positive number.")

    # Calculate the decimal part
    decimal_part = number - int(number)

    return decimal_part


# Example usage:
if __name__ == "__main__":
    try:
        print(truncate_number(3.5))  # Output: 0.5
        print(truncate_number(-3.5))  # Raises ValueError
    except (TypeError, ValueError) as e:
        print(f"Error: {e}")