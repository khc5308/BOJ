n=int(input())
r=0
a=map(int,input().split())
b=map(int,input().split())
for i,j in zip(a,b):
    if j >= i:
        r+=1
print(r)