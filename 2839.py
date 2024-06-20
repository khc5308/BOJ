
#input & 선언
n = int(input())
three = 0
five = 0
tmp = n

if (tmp % 5 == 0 and tmp != 0):
    while tmp != 0:
        tmp -= 5
        five += 1
else:
    while tmp >= 3:
        tmp -= 3
        three += 1
        while tmp % 5 == 0 and tmp != 0:
            tmp -= 5
            five += 1
    
#output
if tmp != 0:
    print(-1)
else:
    print(three+five)