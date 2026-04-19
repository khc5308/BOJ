s = list(input())
check = [1] * len(s)
re = 0
while 1:
    org = ''.join(s)
    l = len(s)
    for i in range(l-1,0,-1):
        #() >> 2
        if s[i] == ')' and s[i-1] == '(':
            s[i] = '2'
            s.pop(i-1)
        #[] >> 3
        elif s[i] == ']' and s[i-1] == '[':
            s[i] = '3'
            s.pop(i-1)
    
    # x + y
    l = len(s)
    for i in range(l-1,0,-1):
        if s[i].isdigit() and s[i-1].isdigit():
            s[i] = str(int(s[i]) + int(s[i-1]))
            s.pop(i-1)

    # (x) or [x]
    t = len(s)-2
    while t > 0:
        if s[t-1] == '(' and s[t].isdigit() and s[t+1] == ')':
            s[t-1] = str(2 * int(s[t]))
            s.pop(t+1)
            s.pop(t)
            t-=2
        elif s[t-1] == '[' and s[t].isdigit() and s[t+1] == ']':
            s[t-1] = str(3 * int(s[t]))
            s.pop(t+1)
            s.pop(t)
            t-=2
        else:
            t-=1
    
    if org == ''.join(s):
        break

print(s[-1] if len(s) == 1 and s[-1].isdigit() else 0)