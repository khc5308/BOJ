def peo(F,ho,arr):
    if arr[F][ho] == 0:
        a = peo(F-1,ho,arr)
        b = peo(F,ho-1,arr)
        arr[F][ho] = a + b
    if arr[F][ho] != 0:
        return arr[F][ho]

t=int(input())
for _ in range(t):
    k = int(input()) #층
    n = int(input()) #호
    arr = [[0 for i in range(n)] for j in range(k+1)]
    for i in range(k+1):
        arr[i][0] = 1
    for j in range (n):
        arr[0][j] = j + 1

    print(peo(k,n-1,arr))