n = int(input())
num = list(map(int, input().split()))
out = 0
def issosu(a : int):
    if a == 1: return False
    for i in range(2,a-1):
        if a%i == 0:
            return False
    return True

for i in range(n):
    if issosu(num[i]):
        out+=1

print(out)