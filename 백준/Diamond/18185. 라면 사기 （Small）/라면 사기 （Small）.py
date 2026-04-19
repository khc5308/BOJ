n = int(input())
a = list(map(int, input().split())) +[0,0]
def t(i):
    m = min(a[i:i+3])
    a[i]-=m
    a[i+1]-=m
    a[i+2]-=m
    return m*7
c = 0
b = True
for i in range(n):
    if a[i+1] > a[i+2]:
        m = min(a[i],(a[i+1]-a[i+2]))
        a[i] -= m
        a[i+1] -= m
        c += m*5
        c += t(i)
    else:
        c += t(i)
        m = min(a[i],a[i+1])
        a[i]-=m
        a[i+1]-=m
        c += m*5
print(c+sum(a)*3)