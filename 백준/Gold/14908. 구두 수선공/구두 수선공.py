import heapq 
n = int(input())
arr = [list(map(int,input().split())) for i in range(n)]
pq = []
for i in range(n):
    heapq.heappush(pq,(-arr[i][1]/arr[i][0], i+1))

for i in range(n):
    print(heapq.heappop(pq)[1], end=" ")