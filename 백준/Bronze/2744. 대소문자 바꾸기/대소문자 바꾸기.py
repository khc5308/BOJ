s = list(input())
for i in range(len(s)):
    if s[i] >= "a" and s[i] <= "z":
        s[i] = s[i].upper()
    else:
        s[i] = s[i].lower()

for i in s:
    print(i,end='')