input()
a=[0,0]
for i in input():
    a[int(i)%2]+=1 
print(1 if a[0]<a[1]else 0 if a[0]>a[1]else -1)