import heapq 
n,k =map(int,input().split())
diamond =[(list(map(int,input().split()))) for i in range(n)]
bag = [int(input()) for i in range(k)]
p = []


bag.sort()
x = 0
r = 0
diamond.sort(key=lambda x : x[0])
for i in bag:
    while x < n:
        if diamond[x][0] <= i:
            heapq.heappush(p,-diamond[x][1])
            x+=1
        else:
            break
    if len(p) >= 1:
        r+=heapq.heappop(p)
    
print(-r)

