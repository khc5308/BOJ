for i in range(int(input())):
    a,b,c,d = map(int,input().split())
    x=b+c+d
    print(a,x,"PASS" if b>10 and c>8 and d>=12 and x>=55 else "FAIL")
