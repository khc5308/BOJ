n=int(input())
s=input()
s1=[]
s2=[]

a=""
right = 0
for i in s:
    right+=[1,-1][i==")"]
    if right < 0:
        s1.append(a)
        a = ""
        right = 0
    else:
        a+=i
s1.append(a)

for i in s1:
    a=""
    right = 0
    for j in range(len(i)-1,-1,-1):
        right+=[1,-1][i[j]=="("]
        if right < 0:
            s2.append(len(a))
            a = ""
            right = 0
        else:
            a=i[j]+a
    s2.append(len(a))
print(max(s2))