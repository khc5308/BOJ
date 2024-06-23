arr = [[0 for j in range(9)] for i in range(9)]

for i in range (9):
    arr[i] = input().split()
for i in range (9):
    for j in range (9):
        arr[i][j] = int(arr[i][j])

print("")

for i in range (9):
    for j in range (9):
        print(arr[i][j], end=' ')
    print("")