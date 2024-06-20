s = input()
korea = ['K','O','R','E','A']
j = 0
out = 0
for i in range (len(s)):
    if s[i] == korea[j]:
        j+=1
        out+=1 
        if (j == 5):
            j = 0
print(out)