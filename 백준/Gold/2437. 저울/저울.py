n=int(input())
a=sorted(map(int,input().split()))
r=1
for i in range(n):
    if r<a[i]:
        break
    r+=a[i]
print(r)