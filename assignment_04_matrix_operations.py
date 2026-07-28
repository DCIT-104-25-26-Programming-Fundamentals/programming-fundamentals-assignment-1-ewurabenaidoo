# =============================================================================
# PROGRAMMING FUNDAMENTALS — Assignment 4
# Topic: Multi-dimensional Arrays (2D Lists), Nested Loops, and Functions
# =============================================================================
#
# TASK: Matrix Operations
#
# Write a Python program that performs three operations on matrices (2D lists),
# each implemented in its own function.
#
# -----------------------------------------------------------------------------
# PART A — Transpose a Matrix
# -----------------------------------------------------------------------------
# - Read an M x N matrix from the user.
# - Compute and display its transpose (rows become columns, columns become rows).
#
# Example (2 x 3 input):
#
#   Original Matrix:      Transposed Matrix:
#   1  2  3               1  4
#   4  5  6               2  5
#                         3  6
#
# -----------------------------------------------------------------------------
# PART B — Add Two Matrices
# -----------------------------------------------------------------------------
# - Read two matrices of exactly the same size (M x N).
# - Compute their element-wise sum and display the result.
#   (Each position in the result = the sum of the values at that position
#    in both matrices.)
#
# -----------------------------------------------------------------------------
# PART C — Multiply Two Matrices
# -----------------------------------------------------------------------------
# - Read matrix A of size M x N and matrix B of size N x P.
#   (The number of COLUMNS in A must equal the number of ROWS in B.)
# - Compute and display the matrix product A × B (result is M x P).
#
# -----------------------------------------------------------------------------
# EXPECTED INPUT FORMAT
# -----------------------------------------------------------------------------
# When entering a row, the user types all values on one line separated by spaces:
#
#   Enter number of rows: 2
#   Enter number of columns: 3
#   Enter row 1: 1 2 3
#   Enter row 2: 4 5 6
#
# -----------------------------------------------------------------------------
# REQUIREMENTS
# -----------------------------------------------------------------------------
# - Use nested loops for all operations (no NumPy or other libraries).
# - Each operation must be in its own function (see scaffold below).
# - Display each matrix in a neat, aligned grid format.
# - Tip: Complete Part A first, then Parts B and C.
#

#
# =============================================================================
# YOUR CODE BELOW — remove the # symbols from the scaffold and fill it in
# =============================================================================


def transpose_matrix(matrix):
    rows = len(matrix)
    cols = len(matrix[0])
    transposed = [[0 for _ in range(rows)] for _ in range(cols)]
    for i in range(rows):
        for j in range(cols):
            transposed[j][i] = matrix[i][j]
    return transposed

def add_matrices(matrix_a, matrix_b):
    rows = len(matrix_a)
    cols = len(matrix_a[0])
    result = [[0 for _ in range(cols)] for _ in range(rows)]
    for i in range(rows):
        for j in range(cols):
            result[i][j] = matrix_a[i][j] + matrix_b[i][j]
    return result

def multiply_matrices(matrix_a, matrix_b):
    rows_a = len(matrix_a)
    cols_a = len(matrix_a[0])
    cols_b = len(matrix_b[0])
    result = [[0 for _ in range(cols_b)] for _ in range(rows_a)]
    for i in range(rows_a):
        for j in range(cols_b):
            for k in range(cols_a):
                result[i][j] += matrix_a[i][k] * matrix_b[k][j]
    return result

def read_matrix(name):
    print(f"\nEntering {name}:")
    rows = int(input("Enter number of rows: "))
    cols = int(input("Enter number of columns: "))
    matrix = []
    for i in range(rows):
        row_input = input(f"Enter row {i + 1}: ")
        row_values = [float(val) for val in row_input.split()]
        matrix.append(row_values)
    return matrix

def print_matrix(matrix):
    for row in matrix:
        formatted_row = "  ".join(f"{int(val) if val.is_integer() else val}" for val in row)
        print(f"  {formatted_row}")

if __name__ == "__main__":
    print("--- PART A: Transpose a Matrix ---")
    matrix_orig = read_matrix("Matrix")
    print("\nOriginal Matrix:")
    print_matrix(matrix_orig)
    transposed_result = transpose_matrix(matrix_orig)
    print("\nTransposed Matrix:")
    print_matrix(transposed_result)
    
    print("\n--- PART B: Add Two Matrices ---")
    print("For addition, both matrices must have the same dimensions.")
    matrix_b1 = read_matrix("Matrix 1")
    matrix_b2 = read_matrix("Matrix 2")
    if len(matrix_b1) != len(matrix_b2) or len(matrix_b1[0]) != len(matrix_b2[0]):
        print("Error: Matrices must have the same dimensions for addition.")
    else:
        addition_result = add_matrices(matrix_b1, matrix_b2)
        print("\nSum Matrix:")
        print_matrix(addition_result)
        
    print("\n--- PART C: Multiply Two Matrices ---")
    print("For multiplication, columns of Matrix A must equal rows of Matrix B.")
    matrix_m1 = read_matrix("Matrix A")
    matrix_m2 = read_matrix("Matrix B")
    if len(matrix_m1[0]) != len(matrix_m2):
        print("Error: Number of columns in Matrix A must equal number of rows in Matrix B.")
    else:
        multiplication_result = multiply_matrices(matrix_m1, matrix_m2)
        print("\nProduct Matrix:")
        print_matrix(multiplication_result)