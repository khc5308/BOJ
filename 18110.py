n = int(input())
diffcult = []
sum = 0

cut_num = n * 0.15
if cut_num - int(cut_num) >= 0.5:
    cut = int(cut_num) + 1
else:
    cut = int(cut_num)

for _ in range (n):
    diffcult.append(int(input()))
diffcult.sort()

for i in range (cut,n - cut,1):
    sum += diffcult[i]

if n == 0:
    print(0)
else:
    num = sum / (n - cut*2)
    if num - int(num) >= 0.5:
        print(int(num) + 1)
    else:
        print(int(num))