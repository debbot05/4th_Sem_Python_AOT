#Find rowwise maximum & columnwise minimum elements.

def find_row_wise_max_and_column_wise_min(matrix):
    # Finding row-wise maximum
    row_max = [max(row) for row in matrix]

    # Finding column-wise minimum
    col_min = [min(col) for col in zip(*matrix)]

    return row_max, col_min

# Example usage
if __name__ == "__main__":
    # Taking a 3x3 matrix as an example
    matrix = [
        [1, 2, 3],
        [4, 5, 6],
        [7, 8, 9]
    ]

    row_max, col_min = find_row_wise_max_and_column_wise_min(matrix)

    print("Row-wise maximum elements:", row_max)
    print("Column-wise minimum elements:", col_min)
