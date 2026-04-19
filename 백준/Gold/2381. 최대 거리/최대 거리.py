n = int(input())
arr = []
for i in range(n):
    a,b = map(int,input().split())
    arr.append([a,b])

arr_x = list(sorted(arr,key=lambda x : x[0]+x[1]))
arr_y = list(sorted(arr,key=lambda x : x[0]-x[1]))

print(max(abs(arr_x[0][0]-arr_x[-1][0]) + abs(arr_x[0][1]-arr_x[-1][1]), 
          abs(arr_y[0][0]-arr_y[-1][0]) + abs(arr_y[0][1]-arr_y[-1][1])))