n=int(input())
arr = list(map(int,input().split()))
r = n
for i in range(n-1):
    for j in range(i+1,n):
        tmp = 0
        d = (arr[j]-arr[i])//(j-i)
        a = arr[i] - i * d
        for k in range(0,n):
            if arr[k] != a + k*d:
                tmp += 1
        r = min(r,tmp)
print(r)