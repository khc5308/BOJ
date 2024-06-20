b1, b2 = map(int,input().split())
c = int(input())

if b1 + b2 >= c*2:
    print((c*2 - b1 - b2)*-1)
else:
    print(b1+b2)