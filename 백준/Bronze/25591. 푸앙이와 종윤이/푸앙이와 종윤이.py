n,m = map(int,input().split())
a=100-n
b=100-m
d=a*b
f="00"+str(n*m)
print(a,b,100-(a+b),d,d//100,d%100)
print(f"{int(f[-4:-2])} {int(f[-2:])}")