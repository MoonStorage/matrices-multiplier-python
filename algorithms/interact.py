import os

# Constants
indentation = "      "


# Functions
def get():

    # Clear Terminal
    os.system("cls")

    # Matrices
    first_matrix = []
    second_matrix = []

    # First matrix
    print("Matrix A:")
    while True:

        # Get input
        command = input(indentation).strip()

        # Check command
        if command == "":
            break
        
        # Parse row
        row_ = command.strip().split(" ")
        row = []

        # Convert to 'float'
        for each in row_:
            row.append(float(each))

        # Append matrix
        first_matrix.append(row)
    
    # Second matrix
    print("Matrix B:")
    while True:

        # Get input
        command = input(indentation).strip()

        # Check command
        if command == "":
            break
        
        # Parse row
        row_ = command.strip().split(" ")
        row = []

        # Convert to 'float'
        for each in row_:
            row.append(float(each))

        # Append matrix
        second_matrix.append(row)
    
    # Return both
    return first_matrix, second_matrix
