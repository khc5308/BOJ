a=input()
l=list(input().split())
re=0
for i in l:
    if i[-1] == a:
        re+=1
print(re)