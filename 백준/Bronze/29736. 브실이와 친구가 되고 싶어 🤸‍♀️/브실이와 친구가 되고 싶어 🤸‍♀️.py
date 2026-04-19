a,b=map(int,input().split())
k,x=map(int,input().split())
n=min(b,k+x)-max(a,k-x)+1
print(n if n>0 else"IMPOSSIBLE")