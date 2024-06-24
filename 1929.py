a, b = map(int,input().split())
# def issosu(a : int):
#     if a == 1: return 0
#     for i in range(2,a-1):
#         if a%i == 0:
#             return 0
#     print(a)
n = [0] * (b+1)
max = int(b**0.5+1)
for i in range (a,b+1):
    n[i] = i
n[1] = 0, 
for i in range (2,max):
    for j in range(a,b+1):
        if j % i == 0:
            n[j] = 0