def sum_up_diagonals(matrix):
    n = len(matrix)  # Get the size of the matrix (number of rows)
    diagonal_sum = 0
    
    for i in range(n):
        diagonal_sum += matrix[i][i]          
        diagonal_sum += matrix[i][n - 1 - i]   
    
    # Since the middle element will be counted twice in odd-sized matrices, we subtract it once
    if n % 2 == 1:
        diagonal_sum -= matrix[n // 2][n // 2]
    
    return diagonal_sum

m1 = [
    [1, 2],
    [30, 40],
]
print(sum_up_diagonals(m1))

m2 = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9],
]
print(sum_up_diagonals(m2)) 
