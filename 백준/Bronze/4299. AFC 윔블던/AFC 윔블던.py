a,b=map(int,input().split())
x=(a+b)/2
y=(a-b)/2

if x == int(x) and y==int(y) and x >= 0 and y >= 0:
    print(int(x),int(y))
else:
    print(-1)
