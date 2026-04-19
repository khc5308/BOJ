import bisect 
import sys
input = sys.stdin.readline
n = int(input())
arr = list(map(int,input().split()))
lis = [-1_000_000_005]
k = []
for i in arr:
    if lis[-1] < i:
        lis.append(i)
        k.append(len(lis)-1)
    else:
        a = bisect.bisect_left(lis,i)
        k.append(a)
        lis[a] = i
r = []
j = max(k)
l = len(k)
for i in range(l-1,-1,-1):
    if j == k[i]:
        r.append(arr[i])
        j-=1

print(len(r))
print(*r[::-1])
    