import sys
s=sys.stdin.read()
a=""
for i in s:
    if i == "i":
        a+="e"
    elif i=="I":
        a+="E"
    elif i=="e":
        a+="i"
    elif i=="E":
        a+="I"
    else:
        a+=i
print(a)