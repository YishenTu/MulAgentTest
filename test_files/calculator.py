def add(a, b):
    """Add two numbers and return the result."""
    return a + b


def subtract(a, b):
    """Subtract b from a and return the result."""
    return a - b


def multiply(a, b):
    """Multiply two numbers and return the result."""
    return a * b


def divide(a, b):
    """Divide a by b and return the result. Handle division by zero."""
    if b == 0:
        raise ValueError("Cannot divide by zero")
    return a / b


def main():
    """Demonstrate all calculator operations."""
    print("Basic Calculator Demo")
    print("=" * 30)
    
    # Addition: 10 + 5
    result = add(10, 5)
    print(f"10 + 5 = {result}")
    
    # Subtraction: 20 - 8
    result = subtract(20, 8)
    print(f"20 - 8 = {result}")
    
    # Multiplication: 6 * 7
    result = multiply(6, 7)
    print(f"6 * 7 = {result}")
    
    # Division: 15 / 3
    result = divide(15, 3)
    print(f"15 / 3 = {result}")
    
    # Demonstrate division by zero handling
    print("\nDivision by zero test:")
    try:
        result = divide(10, 0)
    except ValueError as e:
        print(f"Error: {e}")


if __name__ == "__main__":
    main()