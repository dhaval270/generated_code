def truncate_number(number: float) -> float:
    """
    Given a positive floating point number, it can be decomposed into 
    an integer part (largest integer smaller than given number) and decimals 
    (leftover part always smaller than 1).

    Return the decimal part of the number.
    >>> truncate_number(3.5)
    0.5
    """
    # Check if the input is a positive float
    if not isinstance(number, (int, float)) or number <= 0:
        raise ValueError("Input must be a positive float")
    
    # Calculate the integer part of the number
    integer_part = int(number)
    
    # Calculate the decimal part by subtracting the integer part from the number
    decimal_part = round(number - integer_part, 10)  # Round to 10 decimal places to avoid rounding errors
    
    return decimal_part