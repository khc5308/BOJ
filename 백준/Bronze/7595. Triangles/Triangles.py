import sys
a=map(int,sys.stdin.read().split("\n")[:-1])
for i in a:
    for j in range(1,i+1):
        print("*"*j)