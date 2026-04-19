n,k = map(int,input().split())
arr = []
for i in range(1,int(n**0.5)+1):
    if n % i == 0:
        arr.append(i)
        arr.append(n//i)
arr = sorted(list(set(arr)))

try:
    print(arr[k-1])
except:
    print(0)