n = int(input())
re = 1

while n != 1:
    if (n % 2 == 0):
        n = int(n / 2)
    else:
        n = 3 * n + 1
    re+=1

print(re)