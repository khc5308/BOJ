import bisect 
import sys
input = sys.stdin.readline
n = int(input())
arr = list(map(int,input().split()))
lis = [-1]
for i in arr:
    if lis[-1] < i:
        lis.append(i)
    else:
        a = bisect.bisect_left(lis,i)
        lis[a] = i
print(len(lis)-1)