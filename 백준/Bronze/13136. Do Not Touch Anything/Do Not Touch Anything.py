a,b,c = map(int,input().split())
while 1:
    if a%c == 0 and b%c==0:
        break
    a += 1 if a%c!=0 else 0
    b += 1 if b%c!=0 else 0
print(a*b//c//c)