def gauss(A, b):
    n = len(b)
    Ab = [A[i] + [b[i]] for i in range(n)]
    for k in range(n):

        maxindex = abs(Ab[k][k])
        maxrow = k
        for i in range(k + 1, n):
            if abs(Ab[i][k]) > maxindex:
                maxindex = abs(Ab[i][k])
                maxrow = i

        for j in range(k, n + 1):
            tmp = Ab[maxrow][j]
            Ab[maxrow][j] = Ab[k][j]
            Ab[k][j] = tmp

        for i in range(k + 1, n):
            c = -Ab[i][k] / Ab[k][k]
            for j in range(k, n + 1):
                if j == k:
                    Ab[i][j] = 0
                else:
                    Ab[i][j] += c * Ab[k][j]

        x = [0 for i in range(n)]
        for i in range(n - 1, -1, -1):
            x[i] = Ab[i][n] / Ab[i][i]
            for k in range(i - 1, -1, -1):
                Ab[k][n] -= Ab[k][i] * x[i]
        return x


A = [[2, -3, 1], [1, 1, -2], [3, -1, 4]]
b = [7, 0, 8]

print(gauss(A, b))
