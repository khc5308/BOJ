for i in range(3):
    w=list(map(int,input().split()))
    a=(w[-3]-w[0])*3600+(w[-2]-w[1])*60+w[-1]-w[2]
    print(a//3600,(a%3600)//60,a%60)