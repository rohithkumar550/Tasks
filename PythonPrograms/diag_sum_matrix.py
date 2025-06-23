def diagonal_sum(matrix):
    n = len(matrix)
    total = 0
    for i in range(n):
        total += matrix[i][i]  # main diagonal
        if i != n - 1 - i:
            total += matrix[i][n - 1 - i]  # secondary diagonal
    return total
