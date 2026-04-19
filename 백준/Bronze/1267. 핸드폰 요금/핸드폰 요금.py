n=int(input())
arr = list(map(int,input().split()))
y = 0
m = 0
for i in arr:
    y += 1 + i // 30
    m += 1 + i // 60
y*= 10
m*= 15

if m<y:
    print("M",m)
elif m>y:
    print("Y",y)
else:
    print("Y M",m)