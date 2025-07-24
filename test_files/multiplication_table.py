#!/usr/bin/env python3
"""
Multiplication Table Generator

This script generates a 10x10 multiplication table with proper formatting
and saves the output to a text file.
"""


def generate_multiplication_table(size=10):
    """
    Generate a multiplication table of the specified size.
    
    Args:
        size (int): The size of the multiplication table (default: 10)
    
    Returns:
        str: The formatted multiplication table as a string
    """
    # Calculate the width needed for the largest number
    max_value = size * size
    cell_width = len(str(max_value)) + 1
    
    # Build the table header
    lines = []
    
    # First row with column headers
    header = " " * cell_width + "|"
    for i in range(1, size + 1):
        header += f"{i:>{cell_width}}"
    lines.append(header)
    
    # Separator line
    separator = "-" * cell_width + "+" + "-" * (cell_width * size)
    lines.append(separator)
    
    # Generate each row
    for row in range(1, size + 1):
        line = f"{row:>{cell_width}}|"
        for col in range(1, size + 1):
            product = row * col
            line += f"{product:>{cell_width}}"
        lines.append(line)
    
    return "\n".join(lines)


def save_to_file(content, filename="multiplication_table.txt"):
    """
    Save the content to a text file.
    
    Args:
        content (str): The content to save
        filename (str): The name of the output file
    """
    with open(filename, 'w') as file:
        file.write(content)
    print(f"Multiplication table saved to {filename}")


def main():
    """Main function to generate and save the multiplication table."""
    # Generate the 10x10 multiplication table
    table = generate_multiplication_table(10)
    
    # Display the table
    print("10x10 Multiplication Table:")
    print(table)
    print()
    
    # Save to file
    save_to_file(table)


if __name__ == "__main__":
    main()