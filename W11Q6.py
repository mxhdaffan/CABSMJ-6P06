def matrix_chain_order(p):
    n = len(p)
    
    # Create DP table
    m = [[0 for i in range(n)] for j in range(n)]

    # L is chain length
    for L in range(2, n):
        for i in range(1, n-L+1):
            j = i + L - 1
            m[i][j] = float('inf')

            for k in range(i, j):
                cost = m[i][k] + m[k+1][j] + p[i-1]*p[k]*p[j]

                if cost < m[i][j]:
                    m[i][j] = cost

    return m[1][n-1]


# Example
p = [10, 30, 5, 60]

result = matrix_chain_order(p)

print("Minimum number of multiplications:", result)