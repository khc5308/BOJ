a,b,v = map(int,input().split())
num = 0
day = 0
while 1:
    num+=a
    day+=1
    if num > v:
        break
    num -= b
    if num < 0:
        num = 0
print (day)