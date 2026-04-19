n,x=map(int,input().split())
a=list(map(int,input().split()))
r=99999
for i in range(n-1):
    r=min(a[i]+a[i+1],r)
print(r*x)