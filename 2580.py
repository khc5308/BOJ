arr = [[0 for j in range(9)] for i in range(9)]

for i in range (9):
    arr[i] = input().split()
for i in range (9):
    for j in range (9):
        arr[i][j] = int(arr[i][j])

for i in range (1,9):
    num_arr_i = []
    num_arr_j = []
    for j in range(9):
        

#0 0 0 0 4 3 0 0 0
#0 0 0 0 0 0 1 0 0
#0 0 0 0 5 0 0 0 0
#0 8 0 7 0 0 0 2 0
#0 6 0 0 0 0 0 0 3
#0 0 0 0 0 0 0 4 0
#0 0 5 8 0 0 6 0 0
#4 0 0 1 0 0 0 0 0
#3 0 0 0 0 0 5 0 0