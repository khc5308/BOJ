print("Gnomes:")
for i in range(int(input())):
    a=list(map(int,input().split()))
    print("Ordered" if a==sorted(a) or a==sorted(a,reverse=1)else"Unordered")
