n = int(input())
arr = list(range(1,n+1))
while len(arr) > 1:
    a = arr[1]
    del arr[0]
    arr.append(a)
    del arr[1]

print(arr[0])