n=int(input())
arr=[]
r=0
for i in range(n):
    arr.append(input())
for i in range(n):
    if input() == arr[i]:
        r+=1
print(r)