import algorithms.interact as interact

# Data
first_matrix, second_matrix = interact.get()

# Classes
class First:

    def block():
        return first_matrix

    def rows():
        return len(first_matrix)

    def columns():
        return len(first_matrix[0])


class Second:

    def block():
        return second_matrix

    def rows():
        return len(second_matrix)

    def columns():
        return len(second_matrix[0])
