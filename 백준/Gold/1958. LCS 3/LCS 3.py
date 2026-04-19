a = input()
b = input()
c = input()

n = len(a)
m = len(b)
l = len(c)

h = [[[0 for i in range(l+1)] for j in range(m+1)] for k in range(n+1)]

for i in range(1,n+1):
    for j in range(1,m+1):
        for k in range(1,l+1):
            if a[i-1] == b[j-1] == c[k-1]:
                h[i][j][k] = h[i-1][j-1][k-1] + 1
            else:
                h[i][j][k] = max(h[i-1][j][k], h[i][j-1][k], h[i][j][k-1])

print(h[n][m][l])