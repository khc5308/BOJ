import sys
input = sys.stdin.readline
n=int(input())
arr=list(map(int,input().split()))
s=set()
r=0
di={}

for i in arr:
    if i in di.keys():
        di[i]+=1
    else:
        di[i]=1

for i in range(n):
    for j in range(i+1,n):
        p = arr[i]+arr[j]
        
        if not(p == arr[i] or p == arr[j]) or (di[p] > 1 and arr[i] != arr[j]) or ( arr[i] == arr[j] and di[p] > 2):
            s.add(p)

for i in arr:
    if i in s:
        r+=1
print(r)