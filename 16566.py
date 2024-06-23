n, m, k = map(int,input().split())
card = input().split()
iron = input().split()
for i in range(m):
    card[i] = int(card[i])
for i in range(k):
    iron[i] = int(iron[i])

card.sort()

#이진 탐색
for i in range(k):
    div_2 = int(m / 2)
    while 1:
        if card[div_2] > iron[k] :
            print()
        else: 
            #card[div_2] <= iron[k]
            print()
 

# 10 7 5 > n,m,k
# 2 5 3 7 8 4 9 > card * m
# 4 1 1 3 8 > iron * k

# 1 ) 시간 초과 
# for i in range (k):
#     tmp = 0
#     for j in card:
#         if iron[i] < j:
#             print(j)
#             del card[tmp]
#             break
#         tmp += 1