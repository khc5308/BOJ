n = int(input())
n = n * 2 - 1
for i in range(n,0,-2):
    print(("*"*i).center(n).rstrip())
for i in range(3,n+1,2):
    print(("*"*i).center(n).rstrip())