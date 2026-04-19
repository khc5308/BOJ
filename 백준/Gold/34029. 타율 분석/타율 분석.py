import math
p,n=input().split()
p=float(p)
n=int(n)
for i in range(n+1):
    r=0
    for j in range(i+1):
        r+=math.comb(n,j) * p**j * (1-p)**(n-j)
        if r>=0.05:
            print(j)
            exit()