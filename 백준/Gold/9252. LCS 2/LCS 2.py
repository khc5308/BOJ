a = input()
b = input()

m = len(a)
n = len(b)

c = [[0 for i in range(n+1)] for i in range(m+1)]
for i in range(1,m+1):
    for j in range(1,n+1):
        if a[i-1] == b[j-1]:
            c[i][j] = c[i-1][j-1] + 1
        else:
            c[i][j] = max(c[i-1][j], c[i][j-1])

r=''
i = m
j = n
while i!=0 and j != 0:
    if c[i][j] != c[i-1][j] and c[i][j] != c[i][j-1]:
        r+=a[i-1]
        i-=1
        j-=1
    elif c[i][j] != c[i][j-1]:
        i-=1
    else:
        j-=1
        
print(c[m][n])
print(r[::-1])