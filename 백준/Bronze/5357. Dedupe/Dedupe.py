for i in "_"*int(input()):
    a=input()
    r="a"
    for i in a:
        if r[-1]!=i:
            r+=i
    print(r[1:])