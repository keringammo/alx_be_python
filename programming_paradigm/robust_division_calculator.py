# robust_division_calculator.py

def safe_divide(numerator, denominator):
    """
    Safely divides two values with error handling.
    
    Args:
        numerator: The numerator value (expected numeric).
        denominator: The denominator value (expected numeric).
    
    Returns:
        str: A message with the result or an appropriate error message.
    """
    try:
        # Convert both inputs to float
        num = float(numerator)
        den = float(denominator)

        # Try division
        result = num / den
        return f"The result of the division is {result}"

    except ZeroDivisionError:
        return "Error: Cannot divide by zero."
    except ValueError:
        return "Error: Please enter numeric values only."
