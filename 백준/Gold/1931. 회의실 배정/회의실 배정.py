n=int(input())
arr = []
for i in range(n):
    s,e = map(int,input().split())
    arr.append([s,e])
arr.sort(key= lambda x: (x[1],x[0]))
last = -1
r=0
for i,j in arr:
    if last==-1:
        r+=1
        last=j
        continue
    if last <= i:
        r+=1
        last=j
print(r)