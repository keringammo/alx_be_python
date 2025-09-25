# arithmetic_operations.py

def perform_operation(num1, num2, operation):
    """
    Perform a basic arithmetic operation between two numbers.

    Parameters:
        num1: The first number (int or float).
        num2: The second number (int or float).
        operation (str): The operation to perform.
                         Options: 'add', 'subtract', 'multiply', 'divide'.

    Returns:
        float | str: The result of the operation, or an error message if invalid.
    """

    if operation == "add":
        return num1 + num2
    elif operation == "subtract":
        return num1 - num2
    elif operation == "multiply":
        return num1 * num2
    elif operation == "divide":
        if num2 == 0:
            return "Error: Division by zero"
        return num1 / num2
    else:
        return "Error: Invalid operation. Use 'add', 'subtract', 'multiply', or 'divide'."
