s = input()
arr,l = list(s),len(s)

if len(set(s)) == 1:
    print(-1)
elif arr == list(reversed(arr)):
    print(l-1)
else:
    print(l)