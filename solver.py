from algorithms.data import First, Second

# Constants
indentation = "      "

# Is multiplication possible?
if First.columns() != Second.rows():
    print("Multiplication not possible! Order doesn't match.")

else:

    # Result matrix
    result_matrix = []

    # Loop through every row in first matrix
    for first_row_index in range(First.rows()):
        
        # Result row
        result_row = []

        # Loop through every column for every nth row of first matrix
        for second_row_column_index in range(Second.columns()):

            # Define current row
            first_row = First.block()[first_row_index]
            second_column = []

            # Loop through each column in second matrix
            for second_row_index in range(Second.rows()):
                second_column.append(Second.block()[second_row_index][second_row_column_index])
            
            # Total product and sum of whole row-column pair
            pair_sum = 0

            # Loop through every element to calculate 'pairSum'
            for pair_sum_index in range(len(first_row)):
                pair_sum += first_row[pair_sum_index] * second_column[pair_sum_index]

            # Append 'pairSum' to result row
            result_row.append(pair_sum)
        
        # Append 'result_row' to 'result_matrix'
        result_matrix.append(result_row)
    
    # Line breaks
    print("")
    print("")
    print("")

    # Result Matrix Heading
    print("Result:")

    # Loop through each row
    for result_row_final in result_matrix:

        # Default value
        final = ""

        # Loop through each element
        for each_element in result_row_final:
            final += str(each_element) + "  "

        # Print row
        print(indentation + final)
